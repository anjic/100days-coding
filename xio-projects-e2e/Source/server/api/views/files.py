from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializer.log_serializer import MgmtLogsSerializer, EventLogsSerializer
from api.models.ise_models import MgmtLogs, EventLogs, ListIse 
import requests
import timeit
import os
import re
from django.db.models import Q
from datetime import datetime
from json import (dumps,loads)
import json

# other library
from api.views.mail import SendMail
from utility.dynamic_url_formation import dynamic_url
from config import (AUTH, HEADER_JSON,
                    HEADER_TEXT, RESOURCE)
from api.models.settings import MailUser
from api.serializer.ise_serializer import IseListSerializer
from xio_ise.local_settings  import (BASE_DIR,XML_DIR)
from utility.xml_to_json_parser import xml_to_json

from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse

req_obj = GenericRequests()
res_obj = ClientResponse()
mail_obj = SendMail()

class MgmtLogList(APIView):
	""" 
	To get management logs for particular ise 
	2017-08-04T12:02:59Z
	"""

	def get(self, request, ise_id, format=None):
		start_time = timeit.default_timer()
		mgmtlog = MgmtLogs.objects.filter(ise_id=ise_id)
		start_date = request.GET.get("start_date")
		end_date = request.GET.get("end_date")
		limit = request.GET.get("limit")
		if start_date and end_date:
			start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
			end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
			mgmtlog = mgmtlog.filter(Q(date_time__range=(start_date, end_date))).distinct()
		elif start_date:
			start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
			mgmtlog = mgmtlog.filter(Q(date_time__gte=(start_date))).distinct()
		elif end_date:
			end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
			mgmtlog = mgmtlog.filter(Q(date_time__lte=(end_date))).distinct()
		elif limit:
			mgmtlog = MgmtLogs.objects.all().order_by('-id')[:limit]
			
		serializer = MgmtLogsSerializer(mgmtlog, many=True)
		(response, status_code) = res_obj.response_formation(serializer.data, status.HTTP_200_OK, time_res=True)
		total_time = timeit.default_timer() - start_time
		if response.has_key('time_taken'):
			response['time_taken']['cortex'] = "0.0s"
			response['time_taken']['python'] = "%.2fs"%total_time
			response['time_taken']['total'] = "%.2fs"%total_time
			response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
			response['time_taken']['req_recv_time'] = "%d"%int(start_time)
		return Response(response, status_code)


class EventLogList(APIView):
	""" To get event logs for particular ise """

	def get(self, request, ise_id, format=None):
		start_time = timeit.default_timer()
		eventlog = EventLogs.objects.filter(ise_id=ise_id)
		start_date = request.GET.get("start_date")
		end_date = request.GET.get("end_date")
		limit = request.GET.get("limit")
		if start_date and end_date:
			start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
			end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
			eventlog = eventlog.filter(Q(date_time__range=(start_date, end_date))).distinct()
		elif start_date:
			start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
			eventlog = eventlog.filter(Q(date_time__gte=(start_date))).distinct()
		elif end_date:
			end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
			eventlog = eventlog.filter(Q(date_time__lte=(end_date))).distinct()
		elif limit:
			eventlog = EventLogs.objects.all().order_by('-id')[:limit]

		serializer = EventLogsSerializer(eventlog, many=True)
		(response, status_code) = res_obj.response_formation(serializer.data, status.HTTP_200_OK, time_res=True)
		total_time = timeit.default_timer() - start_time
		if response.has_key('time_taken'):
			response['time_taken']['cortex'] = "0.0s"
			response['time_taken']['python'] = "%.2fs"%total_time
			response['time_taken']['total'] = "%.2fs"%total_time
			response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
			response['time_taken']['req_recv_time'] = "%d"%int(start_time)
		return Response(response, status_code)

# class FileList(APIView):
# 	""" To get list of Power files """

# 	def get(self,request,ise_id,format=None):
# 		get_url = dynamic_url(ise_id)
# 		url_dynamic = get_url[0]
# 		AUTH = get_url[1]
# 		url = url_dynamic+RESOURCE['files']
# 		response_data = {}
# 		res  = req_obj.send_request(url,AUTH,headers=HEADER_JSON)
# 		(response,status) = res_obj.client_response(res)
# 		return Response(response,status=status)

# 	def post(self,request,format=None):
# 		pass

class FileDetail(APIView):
	""" """
	def __init__(self):
		self.cortex_start = 0.0
		self.cortex_total = 0.0

	def get_object(self, ise_id, filename):
		"""To get particular object"""
		start_time = timeit.default_timer()
		get_url = dynamic_url(ise_id)

		if get_url == status.HTTP_404_NOT_FOUND:
			(response, status_code) = res_obj.response_formation('ISE Not Found...', status.HTTP_404_NOT_FOUND)
			return Response(response, status=status_code)

		elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
			(response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
			return Response(response, status=status_code)

		else:
			self.cortex_start = timeit.default_timer()
			url_dynamic = get_url[0]
			AUTH = get_url[1]
			url = url_dynamic + RESOURCE['files'] + "/" +filename
			res  = req_obj.send_request(url, AUTH, headers = HEADER_JSON)
			self.cortex_total = timeit.default_timer() - self.cortex_start
			(response,status_code) = res_obj.client_response(res, time_res=True)
			total_time = timeit.default_timer() - start_time
			process_time = total_time - self.cortex_total
			if response.has_key('time_taken'):
				response['time_taken']['req_recv_time'] = "%d"%int(start_time)
				response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
				response['time_taken']['python'] = "%.2fs"%process_time
				response['time_taken']['total'] = "%.2fs"%total_time
				response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
			return Response(response,status=status_code)

	def get(self, request, ise_id,filename, format=None):
		"""Get particular volume based on it's id"""

		return self.get_object(ise_id,filename)


class MIBfiles(APIView):
	"""
	"""
	def __init__(self):
		self.cortex_start = 0.0
		self.cortex_total = 0.0

	def get_object(self, ise_id, filename):
		"""To get particular object"""
		start_time = timeit.default_timer()
		get_url = dynamic_url(ise_id, False)
		ise_name = ListIse.objects.get(id=ise_id).ise_name
		
		data = {
			"ise_name":ise_name,
		 	"filename":filename,
		}

		if get_url == status.HTTP_404_NOT_FOUND:
			(response, status_code) = res_obj.response_formation('ISE Not Found...', status.HTTP_404_NOT_FOUND)
			return Response(response, status=status_code)

		elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
			(response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
			return Response(response, status=status_code)

		else:
			self.cortex_start = timeit.default_timer()
			url_dynamic = get_url[0]
			AUTH = get_url[1]
			url = url_dynamic + RESOURCE['files'] + "/" + filename
			response  = req_obj.send_request(url, AUTH, headers = HEADER_TEXT, to_convert = False)
			self.cortex_total = timeit.default_timer() - self.cortex_start
			data['content'] = response['result']['response'].pop('data')
			response['result']['response']['data'] = data
			(response, status_code) = res_obj.response_formation(response['result']['response']['data'], status.HTTP_200_OK, time_res=True)
			total_time = timeit.default_timer() - start_time
			process_time = total_time - self.cortex_total
			if response.has_key('time_taken'):
				response['time_taken']['req_recv_time'] = "%d"%int(start_time)
				response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
				response['time_taken']['python'] = "%.2fs"%process_time
				response['time_taken']['total'] = "%.2fs"%total_time
				response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
			return Response(response,status=response['result']['status_code'])


	def get(self, request, ise_id,filename, format=None):
		"""Get particular volume based on it's id"""
		
		return self.get_object(ise_id,filename)

class Severity(APIView):

	def __init__(self):

		self.cortex_start = 0.0
		self.cortex_total = 0.0

	def remove(self, ff, ise_id):

		result = re.sub("<!--[\s\S]+?-->", "", ff)
		data = loads(xml_to_json(result))
		for i in range(len(data['CelContent']['EventList'])):
			print data['CelContent']['EventList'][i].get('Severity')

	def get(self, request, ise_id, format = None):

		"""To get particular object"""
		start_time = timeit.default_timer()
		get_url = dynamic_url(ise_id)

		if get_url == status.HTTP_404_NOT_FOUND:
			(response, status_code) = res_obj.response_formation('ISE Not Found...', status.HTTP_404_NOT_FOUND)
			return Response(response, status=status_code)

		elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
			(response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
			return Response(response, status=status_code)

		else:
			self.cortex_start = timeit.default_timer()
			url_dynamic = get_url[0]
			AUTH = get_url[1]
			url = url_dynamic + RESOURCE['files'] + "/downloads/celxml"
			res  = req_obj.send_request(url, AUTH, headers = HEADER_JSON, to_convert = False, celxml=True)
			ise_name = ListIse.objects.get(id=ise_id).ise_name
			xml_file_name = ise_name+'.xml'
			json_file_name = ise_name+'.json'
			
			if os.path.exists(BASE_DIR + '/xmltojson'):
				with open (XML_DIR + xml_file_name,'w') as f:
					f.write(str(res))
				with open (XML_DIR + xml_file_name,'r') as f:
					temp = f.read()
					self.remove(str(temp),ise_id)
			else:
				os.makedirs(BASE_DIR + '/xmltojson')
				with open (XML_DIR + xml_file_name,'w') as f:
					f.write(res)
				with open (XML_DIR + xml_file_name,'r') as f:
					temp = f.read()
					self.remove(str(temp),ise_id)
			return Response(response,status=status_code)