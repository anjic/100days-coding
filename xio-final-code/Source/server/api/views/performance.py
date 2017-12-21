from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import collections
from influxdb import InfluxDBClient
from api.models.ise_models import (ListIse)
import timeit

# other library
from utility.dynamic_url_formation import dynamic_url
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE, ARRAYCHART)

client = InfluxDBClient('localhost', 8086, 'root', 'password', 'xio_metric')
req_obj = GenericRequests()
res_obj = ClientResponse()


class PerformanceList(APIView):
    '''To get Performance List '''

    def __init__(self):
        '''This initializes the class instance'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting Performance list'''
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
            url = url_dynamic + RESOURCE['performance']
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


class HostIopsChart(APIView):
    '''To get WWN IOPS chart details'''

    def get(self, request, id, host_name, format=None):
        '''This is for getting WWN IOPS chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)

        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readiops'] = '#ff7f0e'
        column_list['writeiops'] = '#2ca02c'
        column_list['totaliops'] = '#7777ff'
        metric_data = fetch_host_data(column_list, id, host_name)

        for data in metric_data:
            if data.get('key') == 'readiops':
                data['key'] = ARRAYCHART['readiops']
            elif data.get('key') == 'writeiops':
                data['key'] = ARRAYCHART['writeiops']
            else:
                data['key'] = ARRAYCHART['totaliops']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class HostDataRateChart(APIView):
    '''To get WWN DataRate chart details'''

    def get(self, request, id, host_name, format=None):
        '''This is for getting WWN DataRate chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readkbps'] = '#ff7f0e'
        column_list['writekbps'] = '#2ca02c'
        column_list['totalkbps'] = '#7777ff'
        metric_data = fetch_host_data(column_list, id, host_name)

        for data in metric_data:
            if data.get('key') == 'readkbps':
                data['key'] = ARRAYCHART['readkbps']
            elif data.get('key') == 'writekbps':
                data['key'] = ARRAYCHART['writekbps']
            else:
                data['key'] = ARRAYCHART['totalkbps']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time        
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class HostQueueDepthChart(APIView):
    '''To get WWN QueueDepth chart details'''

    def get(self, request, id, host_name, format=None):
        '''This is for getting WWN QueueDepth chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['queuedepth'] = '#ff7f0e'
        metric_data = fetch_host_data(column_list, id, host_name)

        for data in metric_data:
            if data.get('key') == 'queuedepth':
                data['key'] = ARRAYCHART['queuedepth']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class HostLatencyChart(APIView):
    '''To get WWN Latency chart details'''

    def get(self, request, id, host_name, format=None):
        '''This is for getting WWN Latency chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readlatency'] = '#ff7f0e'
        column_list['writelatency'] = '#2ca02c'
        metric_data = fetch_host_data(column_list, id, host_name)

        for data in metric_data:
            if data.get('key') == 'readlatency':
                data['key'] = ARRAYCHART['readlatency']
            else:
                data['key'] = ARRAYCHART['writelatency']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


def fetch_host_data(column_list, id, host_name):
    '''This is for fetching WWN data from influxdb based on it's id and ise id'''
    ise_obj = ListIse.objects.get(id=id)
    query = """select time,%s
               from hosts
               where ise_global_id='%s' and host_name = '%s'
               and time > now() - 24h""" % (','.join(column_list),
                                          ise_obj.serial_no, host_name)
    result = client.query(query)
    metric_data = []
    counter = 0
    for key, color in column_list.iteritems():
        metric_data.append({'key': key, 'color': color, 'values': [{'x': result['time'], 'y': 10}]})
        for array_data in result:
            for data in array_data:
                metric_data[counter]['values'].append({'x': data['time'], 'y': data[key]})
        counter = counter + 1
    return metric_data


class VolumeIopsChart(APIView):
    '''To get Volume IOPS chart details'''

    def get(self, request, id, volume_id, format=None):
        '''This is for getting Volume IOPS chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readiops'] = '#ff7f0e'
        column_list['writeiops'] = '#2ca02c'
        column_list['totaliops'] = '#7777ff'
        metric_data = fetch_volume_data(column_list, id, volume_id)

        for data in metric_data:
            if data.get('key') == 'readiops':
                data['key'] = ARRAYCHART['readiops']
            elif data.get('key') == 'writeiops':
                data['key'] = ARRAYCHART['writeiops']
            else:
                data['key'] = ARRAYCHART['totaliops']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class VolumeDataRateChart(APIView):
    '''To get Volume DataRate chart details'''

    def get(self, request, id, volume_id, format=None):
        '''This is for getting Volume DataRate chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readkbps'] = '#ff7f0e'
        column_list['writekbps'] = '#2ca02c'
        column_list['totalkbps'] = '#7777ff'
        metric_data = fetch_volume_data(column_list, id, volume_id)

        for data in metric_data:
            if data.get('key') == 'readkbps':
                data['key'] = ARRAYCHART['readkbps']
            elif data.get('key') == 'writekbps':
                data['key'] = ARRAYCHART['writekbps']
            else:
                data['key'] = ARRAYCHART['totalkbps']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class VolumeQueueDepthChart(APIView):
    '''To get Volume QueueDepth chart details'''

    def get(self, request, id, volume_id, format=None):
        '''This is for getting Volume QueueDepth chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['queuedepth'] = '#ff7f0e'
        metric_data = fetch_volume_data(column_list, id, volume_id)

        for data in metric_data:
            if data.get('key') == 'queuedepth':
                data['key'] = ARRAYCHART['queuedepth']
        
        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class VolumeLatencyChart(APIView):
    '''To get Volume Latency chart details'''

    def get(self, request, id, volume_id, format=None):
        '''This is for getting Volume Latency chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readlatency'] = '#ff7f0e'
        column_list['writelatency'] = '#2ca02c'
        metric_data = fetch_volume_data(column_list, id, volume_id)

        for data in metric_data:
            if data.get('key') == 'readlatency':
                data['key'] = ARRAYCHART['readlatency']
            else:
                data['key'] = ARRAYCHART['writelatency']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


def fetch_volume_data(column_list, id, volume_id):
    '''This is for fetching Volume chart data from influxdb based on it's id and ise id'''
    ise_obj = ListIse.objects.get(id=id)
    query = """select time,%s
               from volumes
               where ise_global_id='%s' and volume_global_id = '%s'
               and time > now() - 24h""" % (','.join(column_list),
                                           ise_obj.serial_no, volume_id)
    result = client.query(query)
    metric_data = []
    counter = 0
    for key, color in column_list.iteritems():
        metric_data.append({'key': key, 'color': color, 'values': [{'x': result['time'], 'y': 10}]})
        for array_data in result:
            for data in array_data:
                metric_data[counter]['values'].append({'x': data['time'], 'y': data[key]})
        counter = counter + 1
    return metric_data


class ControllerIopsChart(APIView):
    '''To get Controller IOPS chart details'''

    def get(self, request, id, controller_id, format=None):
        '''This is for getting Controller IOPS chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readiops'] = '#ff7f0e'
        column_list['writeiops'] = '#2ca02c'
        column_list['totaliops'] = '#7777ff'
        metric_data = fetch_controller_data(column_list, id, controller_id)

        for data in metric_data:
            if data.get('key') == 'readiops':
                data['key'] = ARRAYCHART['readiops']
            elif data.get('key') == 'writeiops':
                data['key'] = ARRAYCHART['writeiops']
            else:
                data['key'] = ARRAYCHART['totaliops']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class ControllerDataRateChart(APIView):
    '''To get Controller DataRate chart details'''

    def get(self, request, id, controller_id, format=None):
        '''This is for getting Controller DataRate chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readkbps'] = '#ff7f0e'
        column_list['writekbps'] = '#2ca02c'
        column_list['totalkbps'] = '#7777ff'
        metric_data = fetch_controller_data(column_list, id, controller_id)

        for data in metric_data:
            if data.get('key') == 'readkbps':
                data['key'] = ARRAYCHART['readkbps']
            elif data.get('key') == 'writekbps':
                data['key'] = ARRAYCHART['writekbps']
            else:
                data['key'] = ARRAYCHART['totalkbps']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class ControllerQueueDepthChart(APIView):
    '''To get Controller QueueDepth chart details'''

    def get(self, request, id, controller_id, format=None):
        '''This is for getting Controller QueueDepth chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['queuedepth'] = '#ff7f0e'
        metric_data = fetch_controller_data(column_list, id, controller_id)

        for data in metric_data:
            if data.get('key') == 'queuedepth':
                data['key'] = ARRAYCHART['queuedepth']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)


class ControllerLatencyChart(APIView):
    '''To get Controller Latency chart details'''

    def get(self, request, id, controller_id, format=None):
        '''This is for getting Controller Latency chart details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readlatency'] = '#ff7f0e'
        column_list['writelatency'] = '#2ca02c'
        metric_data = fetch_controller_data(column_list, id, controller_id)

        for data in metric_data:
            if data.get('key') == 'readlatency':
                data['key'] = ARRAYCHART['readlatency']
            else:
                data['key'] = ARRAYCHART['writelatency']

        (response, status_code) = res_obj.response_formation(metric_data,
                                                             status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time     
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)

def fetch_controller_data(column_list, id, controller_id):
    '''This is for fetching controller chart data from influxdb based on it's id and ise id'''
    ise_obj = ListIse.objects.get(id=id)
    query = """select time,%s
               from controllers
               where ise_global_id='%s' and controller_id = '%s'
               and time > now() - 24h""" % (','.join(column_list),
                                           ise_obj.serial_no, controller_id)
    result = client.query(query)
    metric_data = []
    counter = 0
    for key, color in column_list.iteritems():
        metric_data.append({'key': key, 'color': color, 'values': [{'x': result['time'], 'y': 10}]})
        for array_data in result:
            for data in array_data:
                metric_data[counter]['values'].append({'x': data['time'], 'y': data[key]})
        counter = counter + 1
    return metric_data

def check_authorization(id):
    '''This is for checking authorization'''
    get_url = dynamic_url(id)
    url_dynamic = get_url[0]
    AUTH = get_url[1]
    res = req_obj.send_request(url_dynamic, AUTH, headers=HEADER_JSON)
    (response, status_code) = res_obj.client_response(res)
    if response['message'] == 'fail':
        if response['result']['error']['status_code'] == 401:
            return response
