from django.core.management.base import BaseCommand
from rest_framework import status
import gevent
from datetime import datetime
import ConfigParser
import logging
import redis

# custom modules
from utility.dynamic_url_formation import dynamic_url
from api.serializer.log_serializer import MgmtLogsSerializer,EventLogsSerializer
from xio_ise.local_settings  import (CONF_DIR,LOG_DIR,log_required)
from api.models.ise_models import ListIse
from api.models.ise_models import MgmtLogs, EventLogs
from api.models.settings import MailUser
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (HEADER_JSON)
from api.views.mail import SendMail
from config import (HEADER_JSON,RDS_DB,RDS_HOST,RDS_PORT)

mail_obj = SendMail()
config_obj = ConfigParser.RawConfigParser()
req_obj = GenericRequests()
res_obj = ClientResponse()

redis_obj = redis.StrictRedis(host=RDS_HOST, port=RDS_PORT, db=RDS_DB)

#logger object creating
logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'alert_mail.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
from xio_ise.email_conf import EmailConfig

class Command(BaseCommand):
    """
    """
    def send_to_mail(self, last_id, serializer, mgmtlog=None, ise_details = {}):

        try:
            to_mail_list = {}
            to_mail_list['normal'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],normal=1)]
            to_mail_list['critical'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],critical=1)]
            to_mail_list['severe'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],severe=1)]
            to_mail_list['error'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],error=1)]
            to_mail_list['warning'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],warning=1)]
            to_mail_list['informational'] = [str(mail.get('email')) for mail in MailUser.objects.values('email').filter(ise_id=ise_details['id'],informational=1)]
            for values in to_mail_list.values():
                if values:
                    is_log_required(info=True, title="to_mail",message=to_mail_list , log=log_required)
                    break

            for alert in serializer.data:
                if str(alert['severity']).lower() == 'normal':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('normal'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('normal'), ise_details['serial_number'])

                elif str(alert['severity']).lower() == 'critical':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('critical'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('critical'), ise_details['serial_number'])

                elif str(alert['severity']).lower() == 'severe':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('severe'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('severe'), ise_details['serial_number'])

                elif str(alert['severity']).lower() == 'error':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('error'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('error'), ise_details['serial_number'])

                elif str(alert['severity']).lower() == 'warning':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('warning'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('warning'), ise_details['serial_number'])

                elif str(alert['severity']).lower() == 'informational':
                    if mgmtlog:
                        self.send_log_mail(alert, to_mail_list.get('informational'), ise_details['serial_number'], mgmtlog=True)
                    else:
                        self.send_log_mail(alert, to_mail_list.get('informational'), ise_details['serial_number'])
                else:
                    pass

                if mgmtlog:
                    log = MgmtLogs.objects.get(id=alert['id'])
                    redis_key = 'last_mgmt_record_id'
                    mail = 'mgmt_mail'
                    
                else:
                    log = EventLogs.objects.get(id=alert['id'])
                    redis_key = 'last_event_record_id'
                    mail = 'eventt_mail'

                for values in to_mail_list.values():
                    if values:
                        is_log_required(info=True, title="old log",message=str(alert['id']) , log=log_required)
                        is_log_required(info=True, title=mail,message=last_id , log=log_required)
                        break

                log_entry = log
                redis_obj.set(redis_key,alert['id'])
                log_entry.is_sent = True
                log_entry.save()

        except Exception as e:
            for values in to_mail_list.values():
                if values:
                    is_log_required(info=False, title="error", message=e, log=log_required)
                    break

    def send_log_mail(self, alert, to_mail_list, serial_number, mgmtlog=None):

        if mgmtlog:
            mail_sub = "Mail from XIO-Mgmt-"+"ISE-"+str(serial_number)
            mgmt_sent = "mgmt mail sent"
            log_desc = 'data'
            log_data = MgmtLogs.objects.get(id=alert['id'])
            redis_log = "last_mgmt_record_id"

        else:
            mail_sub = "Mail from XIO-Event-"+"ISE-"+str(serial_number)
            mgmt_sent = "Event mail sent"
            log_data = EventLogs.objects.get(id=alert['id'])
            log_desc = 'description'
            redis_log = "last_event_record_id"

        try:
            mail_obj.send_custom_mail(sub=mail_sub, mes=alert.get(log_desc,'XIO Mail'), to_mail=to_mail_list)
            if to_mail_list:
                is_log_required(info=True, title=mgmt_sent, message=str(alert['id']), log=log_required)
            log = log_data
            redis_obj.set(redis_log,alert['id'])
            log.is_sent = True
            log.save()

        except Exception as e:
            if to_mail_list:
                is_log_required(info=False, title="error", message=e, log=log_required)

    def handle(self, *args, **options):

        redis_obj.set('last_mgmt_record_id',MgmtLogs.objects.last().id)
        redis_obj.set('last_event_record_id',EventLogs.objects.last().id)

        while True:
            config_obj.read(CONF_DIR +'schedule.cfg')
            
            try:
                log_conf =  dict(config_obj.items('delay'))
            except:
                config_obj.add_section('delay')

            log_conf =  dict(config_obj.items('delay'))
            second = int(log_conf.get('alert_mail', 20))

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
                    threads.append(gevent.spawn(self.mgmt_mail, ise_in))
                    threads.append(gevent.spawn(self.event_mail, ise_in))
                gevent.joinall(threads)
                gevent.sleep(second)
                
            except Exception as e:
                is_log_required(info=False, title="Error",message=e , log=log_required)

    def mgmt_mail(self, ise_info={}):

        last_id = redis_obj.get('last_mgmt_record_id')
        mgmtlog = MgmtLogs.objects.filter(ise_id=ise_info['id'], is_sent=False, id__gte=last_id)
        serializer = MgmtLogsSerializer(mgmtlog, many=True)
        self.send_to_mail(last_id=last_id, serializer=serializer, ise_details=ise_info, mgmtlog=True)

    def event_mail(self, ise_info={}):

        last_id = redis_obj.get('last_event_record_id')
        eventlog = EventLogs.objects.filter(ise_id=ise_info['id'], is_sent=False, id__gte=last_id)
        serializer = EventLogsSerializer(eventlog, many=True)
        self.send_to_mail(last_id=last_id, serializer=serializer, ise_details=ise_info, mgmtlog=False)

def is_log_required(info=True, title = '', message = '', log=log_required):

    email = EmailConfig()
    if email.FROM_MAIL:
        if log_required:
            if info:
                logger.info(title + " %s" %message)
            else:
                logger.error(message)