from django.core.management.base import BaseCommand
import gevent
from rest_framework import status
from json import (loads,dumps)
import json
import logging
import os
import re

from utility.dynamic_url_formation import dynamic_url
from xio_ise.local_settings  import (XIO_DIR, LOG_DIR, BASE_DIR, XML_DIR)
from xio_ise.log_required import is_log_required
from api.models.ise_models import ListIse, MappingTable
from api.serializer.log_serializer import MappingTableSerializer
from api.models.ise_models import ListIse
from utility.xml_to_json_parser import xml_to_json
from config import (AUTH, HEADER_JSON,
                    HEADER_TEXT, RESOURCE)
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse

logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'severity_map.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
req_obj = GenericRequests()
res_obj = ClientResponse()

class Command(BaseCommand):

	def handle(self, *args, **options):
		#logger.info("start time ")
		is_log_required(info=True, message = 'start time ',  logger_info=logger)
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
					ise_info['url'] = dynamic_url(ise.id)
					ise_list.append(ise_info)

			for i, m in enumerate(ise_list):
				threads.append(gevent.spawn(self.collect_event_type, m))

			gevent.joinall(threads)
			#logger.info("end time")
			is_log_required(info=True, message = 'end time ',  logger_info=logger)
			gevent.sleep(2)
			        
		except Exception as e:
			#logger.error(e)
			is_log_required(info=True, message=e,  logger_info=logger)

	def remove(self, xml_data, ise_id):

		try:
			result = re.sub("<!--[\s\S]+?-->", "", xml_data)
			event_data = loads(xml_to_json(result))
			for i in range(len(event_data['CelContent']['EventList'])):
				e_data=event_data['CelContent']['EventList'][i]
				event_map = {}
				event_map['ise_id'] = ise_id
				event_map['een_value'] = e_data.get('EENValue')
				event_map['severity'] = e_data.get('Severity')
				serializer = MappingTableSerializer(data=event_map)
				if serializer.is_valid():
					serializer.save()

				#logger.info(event_map['een_value'])
				is_log_required(info=True, message = event_map['een_value'],  logger_info=logger)
				#logger.info("end time")
				is_log_required(info=True, message = 'end time ',  logger_info=logger)
		except Exception as e:
				#logger.error(e)
				is_log_required(info=True, message=e,  logger_info=logger)

	def collect_event_type(self, ise_info={}):
		"""
		"""
		try:
			if ise_info:
				if ise_info['url'][0]:
					url = ise_info['url'][0] + RESOURCE['files'] +  '/downloads/celxml'
					res  = req_obj.send_request(url, AUTH, headers = HEADER_JSON, to_convert = False, celxml=True)
					ise_name = ListIse.objects.get(id=ise_info['id']).ise_name
					self.remove(str(res),ise_info['id'])
		except Exception as e:
			#logger.error(e)
			is_log_required(info=True, message=e,  logger_info=logger)
