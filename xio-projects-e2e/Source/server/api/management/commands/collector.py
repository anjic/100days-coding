from django.core.management.base import BaseCommand
import gevent
import pickle
import redis
import ConfigParser
from xio_ise.local_settings  import CONF_DIR,LOG_DIR,BASE_DIR
from xio_ise.log_required import is_log_required
import logging
from rest_framework import status


# custom modules
from utility.dynamic_url_formation import dynamic_url
from api.models.ise_models import ListIse
from lib.generic_request import GenericRequests
from config import (HEADER_JSON,RDS_DB,RDS_HOST,RDS_PORT)

req_obj = GenericRequests()
redis_obj = redis.StrictRedis(host=RDS_HOST, port=RDS_PORT, db=RDS_DB)
config_obj = ConfigParser.RawConfigParser()

#logger object creating
logger = logging.getLogger('collector')
hdlr = logging.FileHandler(LOG_DIR + 'collector.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

class Command(BaseCommand):
    """
    """

    def collect_data(self, ise_info={}):
        if ise_info:
            if ise_info['url'][0]:
                url = ise_info['url'][0] + 'performance'
                response = req_obj.send_request(url, ise_info['url'][1], headers=HEADER_JSON)

                if response['message'] == 'success':
                    data = response['result']['response']['data']
                    pickled_object = pickle.dumps(data)
                    redis_obj.set('ise_'+ise_info['serial_number'], pickled_object)

    def handle(self, *args, **options):

        while True:
            config_obj.read(CONF_DIR +'schedule.cfg')
            
            try:
                collect =  dict(config_obj.items('delay'))
            except:
                config_obj.add_section('delay')

            collect =  dict(config_obj.items('delay'))
            second = int(collect.get('collector', 20))
            #logger.info("start time ")
            is_log_required(info=True, message = 'start time ',logger_info=logger)
            
            try:
                threads = []
                ise_list = []
                ises = ListIse.objects.all()

                for ise in ises:
                    ise_info = {}
                    ise_info['serial_number'] = ise.serial_no
                    get_url = dynamic_url(ise.id)
                    if get_url == status.HTTP_404_NOT_FOUND:
                        continue

                    elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                        continue

                    else:
                        ise_info['url'] = get_url
                        ise_list.append(ise_info)

                for i, ise in enumerate(ise_list):
                    threads.append(gevent.spawn(self.collect_data, ise))
                gevent.joinall(threads)
                #logger.info("end time ")
                is_log_required(info=True, message = 'end time ', logger_info=logger)
                gevent.sleep(second)

            except Exception as e:
                #logger.error(e)
                is_log_required(info=True, message=e,  logger_info=logger)
                