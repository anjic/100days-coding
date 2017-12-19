from django.core.management.base import BaseCommand
import os
import sys
import logging
import time
import json
import ConfigParser

from xio_ise.local_settings  import LOG_DIR
from lib.generic_request import GenericRequests
from django.contrib.auth.models import (User, Group, Permission)
from api.models.ise_models import (ListIse, SangroupIse)
from api.serializer.sangroup_serializer import SanGroupSerializer
from utility.encryption import encryption, decryption
from config import (AUTH, HEADER_JSON,
                    ISE_STATUS_CODE, RESOURCE,
                    ISE_STATUS)
from xio_ise.local_settings import CONF_DIR, BASE_DIR, LOG_DIR
from xio_ise.log_required import is_log_required


logger = logging.getLogger('seed log')
hdlr = logging.FileHandler(LOG_DIR + 'dbseed.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


req_obj = GenericRequests()
config = ConfigParser.RawConfigParser()


class Command(BaseCommand):
    """
    """
    ISE_IP = "10.20.238.4"
    ISE_USER = "administrator"
    ISE_PASSWORD = "administrator"
    DEFAULT_USERGROUP = "Administrator"
    DEFAULT_USER = "Administrator"
    DEFAULT_USER_PASS = "made4you"
    DEFAULT_USER_EMAIL = "sample@mail.com"
    DEFAULT_SANGROUP = "MYSAN-GROUP"

    def handle(self, *args, **options):

        try:
            #logger.info("db seed process started")
            is_log_required(info=True, message = 'db seed process started ', logger_info=logger)
            if self.init_config():
                self.create_user_group()
                #logger.info("db seed process completed")
                is_log_required(info=True, message = 'db seed process completed ', logger_info=logger)
                return True
            #logger.info("db seed process failed")
            is_log_required(info=True, message = 'db seed process failed ', logger_info=logger)
        except Exception as e:
            #logger.error(e)
            is_log_required(info=True, message=e,  logger_info=logger)

    def init_config(self):
        """
        """
        if not os.path.exists(BASE_DIR + '/conf'):
            os.makedirs(BASE_DIR + '/conf')

        if not os.path.exists(CONF_DIR + 'db_seed.cfg'):

            config.add_section('dbseed')
            config.set('dbseed', 'ISE_IP', '')
            config.set('dbseed', 'ISE_USER', '')
            config.set('dbseed', 'ISE_PASSWORD', '')
            config.set('dbseed', 'DEFAULT_USERGROUP', '')
            config.set('dbseed', 'DEFAULT_USER', '')
            config.set('dbseed', 'DEFAULT_USER_PASS', '')
            config.set('dbseed', 'DEFAULT_USER_EMAIL', '')
            config.set('dbseed', 'DEFAULT_SANGROUP', '')

            with open(CONF_DIR + 'db_seed.cfg', 'wb') as db_seed:
                config.write(db_seed)

        if not self.read_config():
            #logger.info("invalid ip")
            is_log_required(info=True, message = 'invalid ip ', logger_info=logger)
            return False

        return True


    def read_config(self):
        """
        """
        config.read(CONF_DIR + 'db_seed.cfg')

        if filter(lambda val: val == '',dict(config.items('dbseed')).values()):

            #logger.info("Invalid config file please update it.")
            is_log_required(info=True, message = 'Invalid config file please update it. ', logger_info=logger)
            return False

        self.ISE_IP = config.get('dbseed', 'ISE_IP')
        self.ISE_USER = config.get('dbseed', 'ISE_USER')
        self.ISE_PASSWORD = config.get('dbseed', 'ISE_PASSWORD')
        self.DEFAULT_USERGROUP = config.get('dbseed', 'DEFAULT_USERGROUP')
        self.DEFAULT_USER = config.get('dbseed', 'DEFAULT_USER')
        self.DEFAULT_USER_PASS = config.get('dbseed', 'DEFAULT_USER_PASS')
        self.DEFAULT_USER_EMAIL = config.get('dbseed', 'DEFAULT_USER_EMAIL')
        self.DEFAULT_SANGROUP = config.get('dbseed', 'DEFAULT_SANGROUP')

        logger.warn(dict(config.items('dbseed')))
        return self.is_valid_ip()
        
    def is_valid_ip(self):

        primary_url = "http://" + str(self.ISE_IP) + "/query"
        query_response = req_obj.send_request(primary_url, (self.ISE_USER, self.ISE_PASSWORD), headers=HEADER_JSON)
        if query_response['message'] == 'success':
            return True

        return False

    def create_user_group(self):
        """
        {
            "description": "",
            "id": "",
            "name": "Admin"
        }
        """
        
        group = Group.objects.create(name=self.DEFAULT_USERGROUP)
        #logger.info("user group creation completed")
        is_log_required(info=True, message = 'user group creation completed ', logger_info=logger)
        self.create_user(group.id)


    def create_user(self, group_id):
        """
        {
            "confirmpassword": "made4you",
            "email": "admin@mail.com",
            "first_name": "admin",
            "group_id": 4,
            "id": "",
            "is_active": true,
            "is_staff": true,
            "last_name": "admin",
            "password": "made4you",
            "username": "Admin"
        }

        """
        user_info = {
            "email": self.DEFAULT_USER_EMAIL,
            "group_id": group_id,
            "is_active": True,
            "is_staff": True,
            "password": self.DEFAULT_USER_PASS,
            "username": self.DEFAULT_USER
        }

        user = User.objects.create_user(user_info['username'],
                                            user_info['email'], user_info['password'])
        user.is_active = user_info['is_active']
        user.is_staff = user_info['is_staff']
        user.save()
        user.groups.add(Group.objects.get(id=user_info['group_id']))
        #logger.info("user creation completed")
        is_log_required(info=True, message = 'user creation completed ', logger_info=logger)

        self.create_san_group(user.id)

    def create_san_group(self, user_id):
        """{
                "comment": "Admin",
                "created_by": "1",
                "modified_by": "1",
                "sangroup_id": "",
                "sangroup_name": "Admin"
            }"""

        data = {
                "created_by": user_id,
                "modified_by": user_id,
                "sangroup_name": self.DEFAULT_SANGROUP
            }

        serializer = SanGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        #logger.info("sangroup creation completed")
        is_log_required(info=True, message = 'sangroup creation completed ', logger_info=logger)

        # serializer.data["id"]
        self.create_ise(serializer.data["sangroup_id"])

    def create_ise(self, sangroup_id):
        """
        {
            "primary_ip":"10.20.225.136",
            "secondary_ip":"10.20.225.136",
            "user_name":"muthu",
            "user_password":"xxxx"
        }


        """
        # print "entered"
        primary_url = "http://" + str(self.ISE_IP) + "/query"
        query_response = req_obj.send_request(primary_url, (self.ISE_USER, self.ISE_PASSWORD), headers=HEADER_JSON)
        
        if query_response['message'] == 'success':
            query_response = query_response['result']['response']['data']
            
            try:
                query_detail = query_response['array']
                ise = ListIse()
                ise.ise_name = "MyISE-1"
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
                ise.save()
                ise_id = ise.id

                san = SangroupIse()
                san.ise_id = ise_id
                san.sg_id = sangroup_id
                san.save()
                #logger.info("ise creation completed")
                is_log_required(info=True, message = 'ise creation completed ', logger_info=logger)
                # self.create_volume(serializer.data["id"])

            except Exception as e:
                #logger.error(e)
                is_log_required(info=True, message=e,  logger_info=logger)

