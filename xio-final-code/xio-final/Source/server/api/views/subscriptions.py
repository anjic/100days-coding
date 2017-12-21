from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib
import timeit

# other library
from utility.dynamic_url_formation import dynamic_url
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE)
from utility.global_log import local_logger

req_obj = GenericRequests()
res_obj = ClientResponse()

class SubscriptionsList(APIView):
    """
    """
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):

        # print request.resolver_match.view_name

        start_time = timeit.default_timer()

        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            local_logger.info('%s,%.2fs,%s'%(request.get_full_path(),timeit.default_timer() - start_time,request.resolver_match.view_name))
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            local_logger.info('%s,%.2fs,%s'%(request.get_full_path(),timeit.default_timer() - start_time,request.resolver_match.view_name))
            return Response(response, status=status_code)

        else:
            self.cortex_start = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['subscriptions']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if response.has_key('time_taken'):
                response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                response['time_taken']['python'] = "%.2fs"%process_time
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
           
            local_logger.info('%s,%.2fs,%s'%(request.get_full_path(),timeit.default_timer() - start_time,request.resolver_match.view_name))
            return Response(response, status=status_code)

    def post(self, request, ise_id, format=None):
        """
        {
            "id":"4.4.4.4:483",
            "ssl":"disabled",
            "interval":"1440",
            "type":"telemetry",
            "setting":"disabled"
        }
        """
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            self.cortex_start = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['subscriptions']
            query_string = urllib.urlencode(request.data, doseq=True)
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='POST')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

class SubscriptionsDetails(APIView):
    """
    """    
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, request, ise_id, sub_id, type):

        start_time = timeit.default_timer()
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            self.cortex_start = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['subscriptions'] + "/" + sub_id
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            if response.get('message') == 'success':
                subs_data = response['result']['response']['data']['subscriptions']['subscription']
                if isinstance(subs_data['types'], list):
                    for i in range(len(subs_data['types'])):
                        if subs_data['types'][i]['_attr']['name'] == type:
                            subs_type = subs_data['types'][i]
                            subs_data.pop('types')
                            subs_data['types'] = {}
                            subs_data['types'] = subs_type
                            break

            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if response.has_key('time_taken'):
                response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                response['time_taken']['python'] = "%.2fs"%process_time
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
            return Response(response, status=status_code)

    def get(self, request, ise_id, sub_id, type, format=None):
        return self.get_object(request, ise_id, sub_id,type)

    def put(self, request, ise_id, sub_id, type, format=None):
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            payload = dict(request.data)
            url = url_dynamic + RESOURCE['subscriptions'] + "/" + sub_id
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

    def delete(self, request, ise_id, sub_id, type, format=None):
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            payload = {'type':type}
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['subscriptions'] + "/" + sub_id
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='DELETE')
            (response, status_code) = res_obj.response_formation({'deleted_subscription':sub_id}, status.HTTP_200_OK)
            return Response(response, status=status_code)
