from django.core.management.base import BaseCommand
import gevent
from django.core.exceptions import ObjectDoesNotExist
import sys
import logging
from rest_framework import status

# custom modules
from utility.dynamic_url_formation import dynamic_url
from xio_ise.local_settings  import LOG_DIR
from xio_ise.log_required import is_log_required
from api.models.ise_models import ListIse
from api.models.servermgmt_models import (ServerWwnIse, ServerMgmt)
from lib.generic_request import GenericRequests

logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'wwn_sync.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

req_obj = GenericRequests()

HEADER_JSON = {
    "Content-Type":"application/xml"
}

class Command(BaseCommand):
    """
    """
    def wwn_sync(self, ise_info=[]):

        if ise_info:
            if ise_info['url'][0]:
                wwn_name = []
                wwn_group = []
                url = ise_info['url'][0] + 'hosts'
                response = req_obj.send_request(url, ise_info['url'][1], headers=HEADER_JSON)
                if response.get('message') == 'success':
                    host_res = response['result']['response']['data']['hosts']
                    if host_res.has_key('host'):
                        wwn_name.append(host_res['host']['name'])
                    elif host_res.has_key('hosts'):
                        for hosts in host_res['hosts']:
                            wwn_name.append(hosts['name'])
                    else:
                        pass
                        
                is_log_required(info=True, message = wwn_name,logger_info=logger)
                is_log_required(info=True, message = ise_info['id'],logger_info=logger)
                wwn_server = ServerWwnIse.objects.filter(ise_id_id=ise_info['id'])
                for wwn in wwn_server:
                    wwn_group.append(wwn.wwngroup)
                logger.info(wwn_group)

                for wwn in wwn_group:
                    if not wwn in wwn_name:
                        wwn_g = ServerWwnIse.objects.get(wwngroup=wwn)
                        wwn_g.delete()

    def handle(self, *args, **options):

        while True:
            is_log_required(info=True, message = 'start time ',logger_info=logger)
            try:
                threads = []
                ise_list = []
                ises = ListIse.objects.all()
                for ise in ises:
                    url = dynamic_url(ise.id)
                    if url == status.HTTP_404_NOT_FOUND:
                        continue
                    elif url == status.HTTP_504_GATEWAY_TIMEOUT:
                        continue
                    else:
                        ise_info = {}
                        ise_info['id'] = ise.id
                        ise_info['serial_number'] = ise.serial_no
                        ise_info['url'] = url
                        ise_list.append(ise_info)

                for i, ise_in in enumerate(ise_list):
                    threads.append(gevent.spawn(self.wwn_sync, ise_in))

                gevent.joinall(threads)
                is_log_required(info=True, message = 'end time ',logger_info=logger)
                
            except Exception as e:
                is_log_required(info=True, message = e,logger_info=logger)
