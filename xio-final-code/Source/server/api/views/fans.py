from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import timeit

# other library
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from utility.dynamic_url_formation import dynamic_url
from config import (AUTH, HEADER_JSON, RESOURCE)

req_obj = GenericRequests()
res_obj = ClientResponse()


class FanList(APIView):
    '''To get list of Fans'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting list of Fan details'''
        start_time = timeit.default_timer()
        get_url = dynamic_url(ise_id)

        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation(
                'ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation(
                'Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            self.cortex_start = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['fans']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
            return Response(response, status=status_code)


class FanDetail(APIView):
    '''To get a fan details'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, ise_id, fanid):
        '''This is for getting a particular of Fan detail'''
        start_time = timeit.default_timer()
        get_url = dynamic_url(ise_id)

        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation(
                'ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation(
                'Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            self.cortex_start = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['fans'] + "/" + fanid
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
            return Response(response, status=status_code)

    def get(self, request, ise_id, fanid, format=None):
        '''This is for getting Fan details'''
        return self.get_object(ise_id, fanid)

    def put(self, request, ise_id, fanid, format=None):
        '''This is for update particular fan based on it's id
        {
                "led":"disabled"
        }
        '''
        get_url = dynamic_url(ise_id)

        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation(
                'ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation(
                'Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            payload = dict(request.data)
            url = url_dynamic + RESOURCE['fans'] + "/" + fanid
            res = req_obj.send_request(
                url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.response_formation(
                {'fans updated': fanid}, status.HTTP_200_OK)
        return Response(response, status=status_code)
