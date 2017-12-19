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


class PoolsList(APIView):
    '''To get all StoragePools'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting list of all StoragePools'''
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
            url = url_dynamic + RESOURCE['pools']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
            return Response(response, status=status_code)

    def post(self, request, ise_id, format=None):
        '''This is for creating StoragePools'''
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
            url = url_dynamic + RESOURCE['pools']
            query_string = urllib.urlencode(request.data, doseq=True)
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='POST')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)


class PoolsDetail(APIView):
    '''Retrieve,Update or Delete a pools instance'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, ise_id, pool_id):
        '''This is for getting particular Pool object'''
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
            url = url_dynamic + RESOURCE['pools'] + "/" + pool_id
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d" % int(start_time)
            return Response(response, status=status_code)

    def get(self, request, ise_id, pool_id, format=None):
        '''This is for getting particular pools based on it's id'''
        return self.get_object(ise_id, pool_id)

    def put(self, request, ise_id, pool_id, format=None):
        '''Update particular volume based on it's id'''
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
            url = url_dynamic + RESOURCE['pools'] + "/" + pool_id
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

    def delete(self, request, ise_id, pool_id, format=None):
        '''This is for deleting particular pool based on it's id'''
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
            url = url_dynamic + RESOURCE['pools'] + "/" + pool_id
            res = req_obj.send_request(
                url, AUTH, headers=HEADER_JSON, method='DELETE')
            if res['message'] == 'success':
                (response, status_code) = res_obj.response_formation({'deleted_pool': pool_id}, status.HTTP_200_OK)
                return Response(response, status=status_code)
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)


class PoolsChart(APIView):
    '''To get pools chart details'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting pools chart details'''
        get_url = dynamic_url(ise_id)
        start_time = timeit.default_timer()
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
            url = url_dynamic + RESOURCE['pools']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            pool_total = {}
            if res.get('message') == 'success':
                data = res['result']['response']['data']['pools']
                if 'pool' in data:
                    total_size = int(
                        data['pool']['available']['_attr']['total']) + int(
                        data['pool']['used']['_attr']['total'])
                    pool_total = {
                        'overall_total': int(
                            data['pool']['available']['_attr']['total']),
                        'overall_used': int(
                            data['pool']['used']['_attr']['total']),
                        'overall_size': total_size,
                        'pool_size': int(
                            data['pool']['size'])}
                    res['result']['response']['data'].pop('pools')
                    res['result']['response']['data'].update(pool_total)
                else:
                    pool_list = data['pools']
                    sum_free = 0
                    sum_used = 0
                    sum_size = 0
                    size = 0
                    for pool in pool_list:
                        sum_free = sum_free + \
                            int(pool['available']['_attr']['total'])
                        sum_used = sum_used + \
                            int(pool['used']['_attr']['total'])
                        size = size + int(pool['size'])
                        sum_size = sum_size + \
                            (int(pool['available']['_attr']['total']) + int(pool['used']['_attr']['total']))
                    pool_total = {
                        'overall_total': sum_free,
                        'overall_used': sum_used,
                        'overall_size': sum_size,
                        'pool_size': size
                    }
                    res['result']['response']['data'].pop('pools')
                    res['result']['response']['data'].update(pool_total)

                (response, status_code) = res_obj.client_response(res, time_res=True)
                total_time = timeit.default_timer() - start_time
                process_time = total_time - self.cortex_total
                if 'time_taken' in response:
                    response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                    response['time_taken']['python'] = "%.2fs" % process_time
                    response['time_taken']['total'] = "%.2fs" % total_time
                    response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
                    response['time_taken']['req_recv_time'] = "%d" % int(start_time)
                return Response(response, status=status_code)
            else:
                (response, status_code) = res_obj.client_response(res)
                return Response(response, status=status_code)


class DataReduction(APIView):
    '''To get DataReduction'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting datareduction based on it's ise_id'''
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
            url = url_dynamic + RESOURCE['datareduction']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d" % int(start_time)
            return Response(response, status=status_code)
