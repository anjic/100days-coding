from django.core.management.base import BaseCommand
import os
import subprocess
import sys
import logging
import time
import json
import ConfigParser
from django.db.models import Q
from api.models.sangroup_models import SanGroup

from xio_ise.local_settings  import LOG_DIR
from lib.generic_request import GenericRequests
from django.contrib.auth.models import (User, Group, Permission)
from api.models.ise_models import (ListIse, SangroupIse)
from api.serializer.sangroup_serializer import SanGroupSerializer
from utility.encryption import encryption, decryption
from config import HEADER_JSON
from xio_ise.local_settings import CONF_DIR, BASE_DIR
from xio_ise.log_required import is_log_required

logger = logging.getLogger('default ise log')
hdlr = logging.FileHandler(LOG_DIR + 'default_ise.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

req_obj = GenericRequests()



class Command(BaseCommand):
    """
    """
    ISE_IP = subprocess.check_output(
        "dmidecode -t 1 | awk '/SKU/ {printf $3}'", shell=True)
    ISE_PASSWORD = "administrator"
    ISE_USER = "administrator"
    DEFAULT_SANGROUP = "Default"

    def add_arguments(self, parser):
        parser.add_argument('--ip', type=str,
            help='Default ISE IP address')
        parser.add_argument('--sangroup', type=str,
            help='Default ISE SAN Group')
        parser.add_argument('--user', type=str,
            help='Default ISE user name')
        parser.add_argument('--password', type=str,
            help='Default ISE user password')

    def handle(self, *args, **options):
        if options['ip']:
            self.ISE_IP = options['ip']
        if options['sangroup']:
            self.DEFAULT_SANGROUP = options['sangroup']
        if options['user']:
            self.ISE_USER = options['user']
        if options['password']:
            self.ISE_PASSWORD = options['password']

        try:
            #logger.info("db seed process started")
            is_log_required(info=True, message = 'db seed process started ', logger_info=logger)
            if self.is_valid_ip():
                self.create_san_group()
                #logger.info("db seed process completed successfully")
                is_log_required(info=True, message = 'db seed process completed successfully ', logger_info=logger)
        except Exception as e:
            #logger.error(e)
            is_log_required(info=True, message=e,  logger_info=logger)

    
        
    def is_valid_ip(self):

        primary_url = "http://" + str(self.ISE_IP) + "/query"
        query_response = req_obj.send_request(primary_url, (self.ISE_USER, self.ISE_PASSWORD), headers=HEADER_JSON)
        if query_response['message'] == 'success':
            return True

        return False


    def create_san_group(self):
        """
        """

        data = {
                "created_by": 1,
                "modified_by": 1,
                "sangroup_name": self.DEFAULT_SANGROUP
            }

        serializer = SanGroupSerializer(data=data)
        if serializer.is_valid():
            if serializer.save():
                #logger.info("sangroup creation completed:%s"%serializer.data["sangroup_id"])
                is_log_required(info=True, message = 'sangroup creation completed:%s'%serializer.data["sangroup_id"], logger_info=logger)
                self.create_ise(serializer.data["sangroup_id"])
        else:
            #logger.info("'%s' sangroup is already existed:"%self.DEFAULT_SANGROUP)
            is_log_required(info=True, message = '%s sangroup is already existed:'%self.DEFAULT_SANGROUP, logger_info=logger)
            sangroup = SanGroup.objects.get(sangroup_name=self.DEFAULT_SANGROUP)
            self.create_ise(sangroup.sangroup_id)


    def create_ise(self, sangroup_id):
        """
        """
        primary_url = "http://" + str(self.ISE_IP) + "/query"
        query_response = req_obj.send_request(primary_url, (self.ISE_USER, self.ISE_PASSWORD), headers=HEADER_JSON)

        if query_response['message'] == 'success':
            query_response = query_response['result']['response']['data']

            ise_primary_ip = ListIse.objects.filter(
                Q(ip_primary=query_response['array']['controllers']['controllers'][0]['ipaddress']) | Q(
                    ip_primary=query_response['array']['controllers']['controllers'][1]['ipaddress'])).first()
            ise_secondary_ip = ListIse.objects.filter(
                Q(ip_secondary=query_response['array']['controllers']['controllers'][1]['ipaddress']) | Q(
                    ip_secondary=query_response['array']['controllers']['controllers'][0]['ipaddress'])).first()

        if ise_primary_ip:
            #logger.info("'%s' ise already exist."%self.ISE_IP)
            is_log_required(info=True, message = '%s ise already exist.'%self.ISE_IP, logger_info=logger)
            san = SangroupIse()
            san.ise_id = ise_primary_ip.id
            san.sg_id = sangroup_id
            san.save()
            ise = ListIse.objects.get(id=ise_primary_ip.id)
            ise.prefered = True
            ise.save()
            return
        elif ise_secondary_ip:
            #logger.info("'%s' ise already exist."%self.ISE_IP)
            is_log_required(info=True, message = "%s ise already exist."%self.ISE_IP, logger_info=logger)
            san = SangroupIse()
            san.ise_id = ise_primary_ip.id
            san.sg_id = sangroup_id
            san.save()
            ise = ListIse.objects.get(id=ise_secondary_ip.id)
            ise.prefered = True
            ise.save()
            return
        else:
            try:
                id_list = []
                query_detail = query_response['array']
                ise = ListIse()
                ise_list = ListIse.objects.filter(prefered=1)
                ise.ise_name = query_detail['name']
                ise.raw_data = json.dumps(query_response)
                ise.serial_no = query_detail['serialnumber']
                ise.ip_primary = query_detail['controllers']['controllers'][0]['ipaddress']
                if ise.ip_primary is not None:
                    primary_url = "https://" + str(ise.ip_primary) + "/query"
                    res = req_obj.send_request(primary_url, None, headers=HEADER_JSON)

                    if res['message'] == 'success':
                        ise.mrc1_status = True
                    else:
                        ise.mrc1_status = False
                else:
                    ise.mrc1_status = False
                if query_detail['controllers']['controllers'][1]['ipaddress']:
                    ise.ip_secondary = query_detail['controllers']['controllers'][1]['ipaddress']

                if ise.ip_secondary is not None:
                    secondary_url = "https://" + str(ise.ip_secondary) + "/query"
                    res = req_obj.send_request(secondary_url, None, headers=HEADER_JSON)
                    if res['message'] == 'success':
                        ise.mrc2_status = True
                    else:
                        ise.mrc2_status = False
                else:
                    ise.mrc2_status = False

                ise.username = self.ISE_USER
                ise.password = encryption(self.ISE_PASSWORD)
                ListIse.objects.filter(id__in=id_list).update(prefered=False)
                ise.prefered = True
                ise.save()
                ise_id = ise.id

                san = SangroupIse()
                san.ise_id = ise_id
                san.sg_id = sangroup_id
                san.save()
                #logger.info("ise creation completed")
                is_log_required(info=True, message = 'ise creation completed ', logger_info=logger)

            except Exception as e:
                #logger.error(e)
                is_log_required(info=True, message=e,  logger_info=logger)

