import os
import subprocess
import sys
import gevent
import logging
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

# custom modules
from utility.dynamic_url_formation import dynamic_url
from xio_ise.local_settings  import LOG_DIR
from xio_ise.log_required import is_log_required
from api.models.ise_models import (ListIse,StorageCount)
from lib.generic_request import GenericRequests

logger = logging.getLogger('log')
hdlr = logging.FileHandler(LOG_DIR + 'mrc_sync.log')
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
	def update_mrc_status(self, ise):

		ise = ListIse.objects.get(id=ise.get('id'))

		# print ise.get('id'),ise.get('mrc1_status'),ise.get('mrc1_status')
		# print ise.id,ise.mrc1_status,ise.mrc2_status,ise.ip_primary,ise.ip_secondary

		mrc1_ping_response = subprocess.Popen(['ping', str(ise.ip_primary), '-c', '6', "-W", "6"],
											shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		mrc1_ping_response.wait()
		
		ise.mrc1_status = True if mrc1_ping_response.poll() == 0 else  False




		mrc2_ping_response = subprocess.Popen(['ping', str(ise.ip_secondary), '-c', '6', "-W", "6"],
											shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		mrc2_ping_response.wait()

		ise.mrc2_status = True if mrc2_ping_response.poll() == 0 else False

		#logger.info("ise id:%s, serial no:%s, mrc1 status (%s) :%d,  mrc2 status (%s) :%d"%(ise.id ,ise.serial_no ,ise.ip_primary
											#,int(ise.mrc1_status) ,ise.ip_secondary ,int(ise.mrc2_status)))
		is_log_required(info=True, message = 'ise id:%s, serial no:%s, mrc1 status (%s) :%d,  mrc2 status (%s) :%d'%(ise.id ,ise.serial_no ,ise.ip_primary
											,int(ise.mrc1_status) ,ise.ip_secondary ,int(ise.mrc2_status)), logger_info=logger)

		ise.save()
		


	def handle(self, *args, **options):
		while True:
			#logger.info("mrc sync process started")
			is_log_required(info=True, message = 'mrc sync process started ',  logger_info=logger)
			threads = []

			ises = ListIse.objects.all()
			for i,ise in enumerate(ises):
				threads.append(gevent.spawn(self.update_mrc_status, ise.__dict__))
				
			gevent.joinall(threads)
			#logger.info("mrc sync process completed")
			is_log_required(info=True, message = 'mrc sync process completed ',  logger_info=logger)
			gevent.sleep(20)

	