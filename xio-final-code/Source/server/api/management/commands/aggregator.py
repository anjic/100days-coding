from django.core.management.base import BaseCommand
from influxdb import InfluxDBClient
from datetime import datetime
from pytz import timezone
import gevent
import pickle
import redis
import random
import copy
import logging
import ConfigParser

# custom modules
from api.models.ise_models import ListIse
from lib.generic_request import GenericRequests
from config import (HEADER_JSON,INFLUX_USER,
                    INFLUX_PASSWORD,INFLUX_DBNAME,
                    INFLUX_HOST,INFLUX_PORT,
                    RDS_DB,RDS_HOST,RDS_PORT)
from xio_ise.local_settings  import CONF_DIR,LOG_DIR
from xio_ise.log_required import is_log_required

#creating logger object
logger = logging.getLogger('collector')
hdlr = logging.FileHandler(LOG_DIR + 'aggregator.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

config_obj = ConfigParser.RawConfigParser()
req_obj = GenericRequests()
redis_obj = redis.StrictRedis(host=RDS_HOST, port=RDS_PORT, db=RDS_DB)
client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT, INFLUX_USER, INFLUX_PASSWORD, INFLUX_DBNAME)

class Command(BaseCommand):
    """
    """

    def get_from_redis(self, ise_info={}):
        key = 'ise_' + ise_info['serial_number']
        try:
            value = pickle.loads(redis_obj.get(key))
            # redis_obj.expire(key, 20)
            return (key, value)
        except:
            return None

    def get_array_dedup_metric(self, data, globalid, date_time, time_zone):
        array_dedup_metric = {}
        array_dedup_metric['measurement'] = 'dedup'
        array_dedup_metric['tags'] = {
            'global_id': globalid
        }
        array_dedup_metric['fields'] = {
            'timestring':date_time,
            'timezone':time_zone,
            'refcnt': random.randint(0,1024),
            'count': random.randint(0,100)
        }
        array_dedup_metric['time'] = date_time
        return array_dedup_metric

    def get_array_metric(self, data, globalid, date_time, time_zone):

        array_metric = {}
        metric = data['performance']['array']
        array_metric['measurement'] = 'arrays'
        array_metric['tags'] = {
            'global_id': globalid
        }
        array_metric['fields'] = {
            'timestring':date_time,
            'timezone':time_zone,
            'readiops': metric['readiops'],
            'writeiops': metric['writeiops'],
            'totaliops': metric['totaliops'],
            'totalkbps': metric['totalkbps'],
            'readkbps': metric['readkbps'],
            'writekbps': metric['writekbps'],
            'readpercent': metric['readpercent'],
            'avgxfrsize': metric['avgxfrsize'],
            'queuedepth': metric['queuedepth'],
            'readlatency': metric['readlatency'],
            'writelatency': metric['writelatency'],
            'readlatencymax': metric['readlatencymax'],
            'writelatencymax': metric['writelatencymax'],
            'queuedepthmax': metric['queuedepthmax'],
            'totaliosincelastboot': metric['totaliosincelastboot'],
            'totalkbsincelastboot': metric['totalkbsincelastboot'],

        }
        array_metric['time'] = date_time
        return array_metric

    def get_volume_metric(self, data, globalid, date_time, time_zone):
        volume_list = []
        volume_series = []
        volume_metric = {}
        performance_volumes = data['performance']['volumes']

        if 'volumes' in performance_volumes:
            volume_list.extend(data['performance']['volumes']['volumes'])

        elif 'volume' in data['performance']['volumes']:
            volume_list.append(data['performance']['volumes']['volume'])

        volume_metric['measurement'] = 'volumes'
        volume_metric['time'] = date_time
        volume_metric['tags'] = {}
        volume_metric['tags']['ise_global_id']= globalid

        for volume in volume_list:
            volume_metric['tags']['volume_global_id']=volume['globalid']
            volume_metric['fields'] = {
                'timestring':date_time,
                'timezone':time_zone,
                'readiops': volume['readiops'],
                'writeiops': volume['writeiops'],
                'totaliops': volume['totaliops'],
                'totalkbps': volume['totalkbps'],
                'readkbps': volume['readkbps'],
                'writekbps': volume['writekbps'],
                'readpercent': volume['readpercent'],
                'avgxfrsize': volume['avgxfrsize'],
                'queuedepth': volume['queuedepth'],
                'readlatency': volume['readlatency'],
                'writelatency': volume['writelatency'],
                'readlatencymax': volume['readlatencymax'],
                'writelatencymax': volume['writelatencymax'],
                'queuedepthmax': volume['queuedepthmax'],
                'totaliosincelastboot': volume['totaliosincelastboot'],
                'totalkbsincelastboot': volume['totalkbsincelastboot']
            }
            volume_series.append(copy.deepcopy(volume_metric))
        return volume_series

    def get_host_metric(self, data, globalid, date_time, time_zone):
        host_list = []
        host_series = []
        performance_host = data['performance']['hosts']

        if 'hosts' in performance_host:
            host_list.extend(performance_host['hosts'])

        elif 'host' in performance_host:
            host_list.append(performance_host['host'])

        for host in host_list:
            host_endpoints = []
            host_metric = {}
            host_metric['measurement'] = 'hosts'
            host_metric['tags'] = {
                'ise_global_id': globalid,
                'host_name': host['name']
            }
            host_metric['fields'] = {
                'timestring':date_time,
                'timezone':time_zone,
                'readiops': 0,
                'writeiops': 0,
                'totaliops': 0,
                'totalkbps': 0,
                'readkbps': 0,
                'writekbps': 0,
                'readpercent': 0,
                'avgxfrsize': 0,
                'queuedepth': 0,
                'readlatency': 0,
                'writelatency': 0,
                'readlatencymax': 0,
                'writelatencymax': 0,
                'queuedepthmax': 0,
                'totaliosincelastboot': 0,
                'totalkbsincelastboot': 0
            }
            host_metric['time'] = date_time

            if 'endpoints' in host['endpoints']:
                host_endpoints.extend(host['endpoints']['endpoints'])

            elif 'endpoint' in host['endpoints']:
                host_endpoints.append(host['endpoints']['endpoint'])

            for endpoint in host_endpoints:
                host_check = any(value == 'NA' for value in endpoint.values())
                if not host_check:
                    host_metric['fields'] = {
                        'timestring':date_time,
                        'timezone':time_zone,
                        'readiops': host_metric['fields']['readiops'] + endpoint['readiops'],
                        'writeiops': host_metric['fields']['writeiops'] + endpoint['writeiops'],
                        'totaliops': host_metric['fields']['totaliops'] + endpoint['totaliops'],
                        'totalkbps': host_metric['fields']['totalkbps'] + endpoint['totalkbps'],
                        'readkbps': host_metric['fields']['readkbps'] + endpoint['readkbps'],
                        'writekbps': host_metric['fields']['writekbps'] + endpoint['writekbps'],
                        'readpercent': host_metric['fields']['readpercent'] + endpoint['readpercent'],
                        'avgxfrsize': host_metric['fields']['avgxfrsize'] + endpoint['avgxfrsize'],
                        'queuedepth': host_metric['fields']['queuedepth'] + endpoint['queuedepth'],
                        'readlatency': host_metric['fields']['readlatency'] + endpoint['readlatency'],
                        'writelatency': host_metric['fields']['writelatency'] + endpoint['writelatency'],
                        'readlatencymax': host_metric['fields']['readlatencymax'] + endpoint['readlatencymax'],
                        'writelatencymax': host_metric['fields']['writelatencymax'] + endpoint['writelatencymax'],
                        'queuedepthmax': host_metric['fields']['queuedepthmax'] + endpoint['queuedepthmax'],
                        'totaliosincelastboot': host_metric['fields']['totaliosincelastboot']
                                                + endpoint['totaliosincelastboot'],
                        'totalkbsincelastboot': host_metric['fields']['totalkbsincelastboot']
                                                + endpoint['totalkbsincelastboot']
                    }
            host_series.append(host_metric)
        return host_series

    def get_controller_metric(self, data, globalid, date_time, time_zone):
        controller_series = []
        controller_list = []
        performance_controller = data['performance']['controllers']

        if 'controllers' in performance_controller:
            controller_list.extend(performance_controller['controllers'])

        elif 'controller' in performance_controller:
            controller_list.append(performance_controller['controller'])

        for controller in controller_list:
            controller_metric = {}
            controller_metric['measurement'] = 'controllers'
            controller_metric['tags'] = {
                'ise_global_id': globalid,
                'controller_id': controller['name']
            }
            controller_metric['fields'] = {
                'timestring':date_time,
                'timezone':time_zone,
                'readiops': controller['readiops'],
                'writeiops': controller['writeiops'],
                'totaliops': controller['totaliops'],
                'totalkbps': controller['totalkbps'],
                'readkbps': controller['readkbps'],
                'writekbps': controller['writekbps'],
                'readpercent': controller['readpercent'],
                'avgxfrsize': controller['avgxfrsize'],
                'queuedepth': controller['queuedepth'],
                'readlatency': controller['readlatency'],
                'writelatency': controller['writelatency'],
                'readlatencymax': controller['readlatencymax'],
                'writelatencymax': controller['writelatencymax'],
                'queuedepthmax': controller['queuedepthmax']
            }
            controller_metric['time'] = date_time
            controller_series.append(controller_metric)
        return controller_series

    def get_metric(self, ise_info={}):

        if ise_info:
            series = []

            if self.get_from_redis(ise_info):
                (key, data) = self.get_from_redis(ise_info)
                globalid = data['performance']['array']['globalid']
                date_time_str = str(data['performance']['date']) + ' ' + str(data['performance']['time'])
                datetime_obj = datetime.strptime(date_time_str, "%m/%d/%Y %H:%M:%S")
                # datetime_obj_tz = datetime_obj.replace(tzinfo=timezone(data['performance']['timezone']))
                date_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
                time_zone = str(data['performance']['timezone'])

                series.append(self.get_array_metric(data, globalid, date_time, time_zone))
                series.append(self.get_array_dedup_metric(data, globalid, date_time, time_zone))
                series.extend(self.get_volume_metric(data, globalid, date_time, time_zone))
                series.extend(self.get_host_metric(data, globalid,date_time, time_zone))
                series.extend(self.get_controller_metric(data, globalid, date_time, time_zone))

                try:
                    if client.write_points(series):
                        redis_obj.delete(key)
                except:
                    client.create_database(INFLUX_DBNAME)
                    if client.write_points(series):
                        redis_obj.delete(key)
                # if client.write_points(series):
                #     redis_obj.delete(key)

    def handle(self, *args, **options):

        while True:
            config_obj.read(CONF_DIR +'schedule.cfg')
            
            try:
                aggregat =  dict(config_obj.items('delay'))
            except:
                config_obj.add_section('delay')

            aggregat =  dict(config_obj.items('delay'))
            second = int(aggregat.get('aggregator', 20))
            #logger.info("start time ")
            is_log_required(info=True, message = 'start time ',logger_info=logger)

            try:
                threads = []
                ise_list = []
                ises = ListIse.objects.all()

                for ise in ises:
                    ise_info = {}
                    ise_info['serial_number'] = ise.serial_no
                    ise_list.append(ise_info)

                for i, m in enumerate(ise_list):
                    threads.append(gevent.spawn(self.get_metric, m))

                gevent.joinall(threads)
                #logger.info("end time ")
                is_log_required(info=True, message = 'end time ',logger_info=logger)
                gevent.sleep(second)

            except Exception as e:
                #logger.error(e)
                is_log_required(info=True, message=e,  logger_info=logger)
