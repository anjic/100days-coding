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
req_obj = GenericRequests()
res_obj = ClientResponse()


class SnmpList(APIView):
    """
    """
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):

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
            url = url_dynamic + RESOURCE['snmp']
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
            return Response(response, status=status_code)

    def post(self, request, ise_id, format=None):
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
            url = url_dynamic + RESOURCE['snmp']
            query_string = urllib.urlencode(request.data, doseq=True)
            res = res_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='post')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

class SnmpUpdate(APIView):
#     """
#     """
#     # def get_object(self, ise_id, drive_id):
#     #     get_url = dynamic_url(ise_id)
#     #     if not type(get_url) is int:
#     #         url_dynamic = get_url[0]
#     #         AUTH = get_url[1]
#     #         url = url_dynamic + RESOURCE['snmp'] + "/" + drive_id
#     #         res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
#     #         (response, status_code) = res_obj.client_response(res)
#     #         return Response(response, status=status_code)
#     #     else:
#     #         (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
#     #         return Response(response, status=status_code)

#     # def get(self, ise_id, drive_id, format=None):
#     #     return self.get_object(ise_id, drive_id)

    def put(self, request, ise_id, format=None):

        try:
            delete_query = request.data.pop('removed_list')
        except:
            delete_query = []

        try:
            post_query = request.data.pop('added_list')
        except:
            post_query = []

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
            
            for p_query in post_query:
                payload = dict({'trap':p_query['_attr']['value']})
                url = url_dynamic + RESOURCE['snmp']
                res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='POST')
                (response, status_code) = res_obj.client_response(res)

            for d_query in delete_query:
                payload = dict({'trap':d_query['_attr']['value']})
                url = url_dynamic + RESOURCE['snmp']
                res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='DELETE')
                (response, status_code) = res_obj.client_response(res)

            payload = request.data
            url = url_dynamic + RESOURCE['snmp']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.client_response(res)

            return Response(response, status=status_code)

class SnmpClient(APIView):
    """
    """
    def post(self, request, ise_id, format=None):

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
            payload = request.data
            url = url_dynamic + RESOURCE['snmp']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='POST')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

class SnmpClientDelete(APIView):
    """
    """
    def post(self, request, ise_id, format=None):

        """
        {
            "client":"1.2.3.6"
        }
        """
        get_url = dynamic_url(ise_id )
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            payload = request.data
            url = url_dynamic + RESOURCE['snmp']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data = payload, method='DELETE')
            (response, status_code) = res_obj.response_formation({'deleted_client':request.data['client']}, status.HTTP_200_OK)
            return Response(response, status=status_code)