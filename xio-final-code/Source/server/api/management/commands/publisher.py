from django.core.management.base import BaseCommand
import json
import gevent
import zmq.green as zmq
import requests
import ConfigParser
import logging
from datetime import datetime

from utility.dynamic_url_formation import dynamic_url
from config import (INFLUX_DBNAME, ISE_ID)
from api.models.ise_models import ListIse
from xio_ise.local_settings  import (CONF_DIR, LOG_DIR)
from xio_ise.log_required import is_log_required
from config import (HEADER_JSON, INFLUX_USER,
                    INFLUX_PASSWORD, INFLUX_DBNAME,
                    INFLUX_HOST, INFLUX_PORT,
                    RDS_DB, RDS_HOST, RDS_PORT,
                    SOCKET_IP, SOCKET_PORT)
from lib.generic_request import GenericRequests
req_obj = GenericRequests()

#creating logger object
logger = logging.getLogger('publisher')
hdlr = logging.FileHandler(LOG_DIR + 'publisher.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

config_obj = ConfigParser.RawConfigParser()

class GraphData(object):

    def get_array_metric(self):

        metric_data = []
        ises = ListIse.objects.all()

        for ise in ises:
            url = dynamic_url(ise.id, https=False, query=True)

            try:
              if type(url) is int:
                #logger.info("invalid url %s"%url)
                is_log_required(info=True, message = 'invalid url %s'%url,  logger_info=logger)
                continue

              ise_metric = {'ise_id':ise.id,'data':[]}
              payload = {}
              time_response = req_obj.send_request(url[0], '', headers=HEADER_JSON)
              data = time_response['result']['response']['data']['array']['chronometer']
              date_time_str = str(data['_attr']['date']) + ' ' + str(data['_attr']['time'])
              curr_time = int(datetime.strptime(date_time_str, '%d-%b-%Y %H:%M:%S').strftime("%s"))
              query = """ SELECT time, readiops, writeiops, totaliops, readlatency, writelatency,
                          readlatencymax, writelatencymax, readkbps, writekbps, totalkbps
                          FROM arrays
                          WHERE global_id = '%s' and time  < %ss
                          ORDER BY time DESC LIMIT 1"""%(ise.serial_no, curr_time)

              payload['db'] = INFLUX_DBNAME
              payload['q'] = query

              response = requests.get('http://%s:%s/query?pretty=true'%(INFLUX_HOST, INFLUX_PORT), params=payload)
              result = json.loads(response.text.encode('utf-8'))

            except:
                #logger.info("ise not ready: %s", url)
                is_log_required(info=True, message = 'ise not ready: %s'%url,  logger_info=logger)
                continue

            try:
                point_list = result['results'][0]['series'][0]['values'][0]
                # logger.info(point_list)
                is_log_required(info=True, message = point_list,  logger_info=logger)
                # logger.info("output result %s"%point_list)
                # import sys
                # sys.exit()

                ise_metric['data'].append({'key': 'readiops',
                                           'color': '#ff7f0e',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[1]
                                                     }]
                                          })
                ise_metric['data'].append({'key': 'writeiops',
                                           'color': '#2ca02c',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[2]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'totaliops',
                                           'color': '#7777ff',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[3]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'readlatency',
                                           'color': '#ff7f0e',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[4]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'writelatency',
                                           'color': '#2ca02c',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[5]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'readlatencymax',
                                           'color': '#7777ff',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[6]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'writelatencymax',
                                           'color': '#7788ff',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[7]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'readkbps',
                                           'color': '#ff7f0e',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[8]
                                                     }]
                                          })
                ise_metric['data'].append({'key': 'writekbps',
                                           'color': '#2ca02c',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[9]
                                                       }]
                                           })
                ise_metric['data'].append({'key': 'totalkbps',
                                           'color': '#7777ff',
                                           'values': [{'series':0,
                                                       'x': point_list[0],
                                                       'y': point_list[10]
                                                       }]
                                           })
                metric_data.append(ise_metric)
            except:
                # logger.info("No data found in influx")
                is_log_required(info=True, message ='No data found in influx',  logger_info=logger)

        return metric_data

class Command(BaseCommand):

    def handle(self, *args, **options):


        try:
            graph = GraphData()
            context = zmq.Context()
            socket = context.socket(zmq.PUB)
            socket.connect("tcp://%s:%s"%(SOCKET_IP,SOCKET_PORT))

            while True:
                config_obj.read(CONF_DIR +'schedule.cfg')
                try:
                  publish =  dict(config_obj.items('delay'))
                except:
                  config_obj.add_section('delay')
                  
                publish =  dict(config_obj.items('delay'))
                second = publish.get('publisher', 20)
                # logger.info("start time ")
                is_log_required(info=True, message ='start time',  logger_info=logger)
                socket.send(json.dumps(graph.get_array_metric()))
                # logger.info("end time")
                is_log_required(info=True, message ='end time',  logger_info=logger)
                # logger.info("delay second: %s"%second)
                is_log_required(info=True, message ='delay second: %s'%second,  logger_info=logger)
                gevent.sleep(int(second))

        except Exception as e:
            #logger.error(e)
            is_log_required(info=True, message=e,  logger_info=logger)
