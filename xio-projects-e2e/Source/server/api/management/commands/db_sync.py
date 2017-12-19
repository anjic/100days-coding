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
from api.models.ise_models import (ListIse,StorageCount)
from lib.generic_request import GenericRequests

logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'dbsync.log')
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
	def card_info(self,ise_info=[]):

		if ise_info:
			response = req_obj.send_request(ise_info[0], ise_info[1], headers=HEADER_JSON)
			if response['message'] == 'success':
				data = response['result']['response']['data']['arrays']

				ise_obj = ListIse.objects.get(id=ise_info[2])
				ise_obj.serial_no = data['array']['globalid']

				if data['array']['name']:
					ise_obj.ise_name = data['array']['name']
				else:
					ise_obj.ise_name = 'ISE-' + data['array']['globalid']
	
				ise_obj.ip_primary = data['array']['ipaddress1']
				ise_obj.ip_secondary = data['array']['ipaddress2']
				ise_obj.contactphone = data['array']['contactphone']
				ise_obj.contactemail = data['array']['contactemail']
				ise_obj.contactname = data['array']['contactname']
				ise_obj.location = data['array']['location']
				ise_obj.address = data['array']['address']
				ise_obj.save()

				if 'hosts' in data['array']['hosts']:
					hosts = len(data['array']['hosts']['hosts'])
				elif 'host' in data['array']['hosts']:
					hosts = 1

				if 'volumes' in data['array']['volumes']:
					volumes = len(data['array']['volumes']['volumes'])
				elif 'volume' in data['array']['volumes']:
					volumes = 1

				if 'endpoints' in data['array']['endpoints']:
					endpoints = len(data['array']['endpoints']['endpoints'])
				elif 'endpoint' in data['array']['endpoints']:
					endpoints = 1

				if 'pools' in data['array']['pools']:
					pools = len(data['array']['pools']['pools'])
				elif 'pool' in data['array']['pools']:
					pools = 1

				try:
					ise_count = StorageCount.objects.get(ise_id=ise_info[2])
					ise_count.hosts = hosts
					ise_count.volumes = volumes
					ise_count.endpoints = endpoints
					ise_count.pools = pools
					ise_count.save()

				except ObjectDoesNotExist:
					ise_count = StorageCount.objects.create(ise_id=ise_obj, hosts=hosts,volumes=volumes,endpoints=endpoints,pools=pools)


	def handle(self, *args, **options):
		while True:
			#logger.info("dbsync process started")
			is_log_required(info=True, message = 'dbsync process started ', logger_info=logger)
			threads = []
			ise_list = []
			ises = ListIse.objects.all()


			for ise in ises:
				get_url = dynamic_url(ise.id)
				if get_url == status.HTTP_404_NOT_FOUND:
					continue

				elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
					continue

				else:
					ise_list.append(get_url)

			#logger.info(ise_list)
			is_log_required(info=True, message = 'ise_list ', logger_info=logger)
			for i,ise in enumerate(ise_list):
				threads.append(gevent.spawn(self.card_info, ise))
				
			gevent.joinall(threads)
			#logger.info("dbsync process completed")
			is_log_required(info=True, message = 'dbsync process completed ', logger_info=logger)
			gevent.sleep(10)

	
