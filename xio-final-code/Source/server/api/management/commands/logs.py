from django.core.management.base import BaseCommand
import gevent
from datetime import datetime
import ConfigParser
import logging

# custom modules
from utility.dynamic_url_formation import dynamic_url
from api.serializer.log_serializer import MgmtLogsSerializer,EventLogsSerializer
from xio_ise.local_settings  import CONF_DIR,LOG_DIR
from xio_ise.log_required import is_log_required
from api.models.ise_models import ListIse,MappingTable
from lib.generic_request import GenericRequests
from config import (HEADER_JSON)

config_obj = ConfigParser.RawConfigParser()
req_obj = GenericRequests()

#logger object creating
logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'log_file.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

class Command(BaseCommand):
    """
    """

    def collect_mgmt_logs(self, ise_info={}):
        """
        """

        if ise_info:
            if ise_info['url'][0]:
                url = ise_info['url'][0] + 'files/mgmt'
                response = req_obj.send_request(url, ise_info['url'][1], headers=HEADER_JSON)

                if response['message'] == 'success':
                    mgmt_list = response['result']['response']['data']['mgmt']['mgmt']

                    for log in mgmt_list:
                        datetime_str = str(log.get('Date')) + ' ' + str(log.get('Time'))
                        datetime_obj = datetime.strptime(datetime_str, "%d-%b-%Y %I:%M:%S %p")
                        event_data = {}
                        event_data['date_time'] = datetime_obj
                        event_data['ise_id'] = ise_info['id']
                        event_data['data'] = "MgmtEvent-Type:%s, Component:%s-%s"%(log['Code'],log['Service'],log['Data'])
                        event_data['status'] = log['Status']
                        event_data['code'] = log['Code']
                        event_data['severity'] = log['Severity']
                        event_data['service'] = log['Service']
                        serializer = MgmtLogsSerializer(data=event_data)

                        if serializer.is_valid():
                            serializer.save()

    def handle(self, *args, **options):

        while True:
            config_obj.read(CONF_DIR +'schedule.cfg')
            
            try:
                log_conf =  dict(config_obj.items('delay'))
            except:
                config_obj.add_section('delay')

            log_conf =  dict(config_obj.items('delay'))
            second = int(log_conf.get('logs', 20))
            #logger.info("start time ")
            is_log_required(info=True, message = 'start time ', logger_info=logger)
            try:
                threads = []
                ise_list = []
                ises = ListIse.objects.all()

                for ise in ises:
                    ise_info = {}
                    ise_info['id'] = ise.id
                    ise_info['serial_number'] = ise.serial_no
                    if not type(dynamic_url(ise.id)) is int:
                        ise_info['url'] = dynamic_url(ise.id)
                        ise_list.append(ise_info)

                for i, m in enumerate(ise_list):
                    threads.append(gevent.spawn(self.collect_mgmt_logs, m))
                    threads.append(gevent.spawn(self.collect_event_logs, m))
                gevent.joinall(threads)
                #logger.info("end time ")
                is_log_required(info=True, message = 'end time ', logger_info=logger)
                gevent.sleep(second)
                                    
            except Exception as e:
                #logger.error(e)
                is_log_required(info=True, message=e,  logger_info=logger)


    def collect_event_logs(self, ise_info={}):
        """
        """
        if ise_info:
            if ise_info['url'][0]:
                url = ise_info['url'][0] + 'files/event'
                response = req_obj.send_request(url, ise_info['url'][1], headers=HEADER_JSON)

                if response['message'] == 'success':
                    event_list = response['result']['response']['data']['event']['event']

                    for log in event_list:
                        datetime_str = str(log.get('date')) + ' ' + str(log.get('time'))
                        datetime_obj = datetime.strptime(datetime_str, "%d-%b-%Y %I:%M:%S %p")
                        event_data = {}
                        event_data['date_time'] = datetime_obj
                        event_data['ise_id'] = ise_info['id']
                        event_data['component'] = log['Component']
                        event_data['event_class'] = log['Class']
                        event_data['event_type'] = log['Type']
                        try:
                            event_severe = MappingTable.objects.filter(ise_id=ise_info['id'],een_value=event_data['event_type'])
                            for event in event_severe:
                                if event.severity == "Info":
                                    event_data['severity']="Informational"
                                elif event.severity == "Debug":
                                    event_data['severity']="Error"
                                else:
                                    event_data['severity']=event.severity
                        except MappingTable.DoesNotExist:
                            event_data['severity']="Severity"
                        event_data['description'] = log['Description']
                        serializer = EventLogsSerializer(data=event_data)

                        if serializer.is_valid():
                            serializer.save()

