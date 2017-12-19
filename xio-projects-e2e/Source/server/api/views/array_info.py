from rest_framework.views import APIView
from rest_framework.response import Response
from influxdb import InfluxDBClient
import random
import collections
from datetime import datetime
from rest_framework import status
import timeit

# other library
from lib.client_response import ClientResponse
from lib.generic_request import GenericRequests
from utility.dynamic_url_formation import dynamic_url
from api.models.ise_models import ListIse
from config import (AUTH,
                    HEADER_JSON,
                    RESOURCE, INFLUX_USER,
                    INFLUX_PASSWORD, INFLUX_DBNAME,
                    INFLUX_HOST, INFLUX_PORT,
                    ARRAYCHART)

client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT,
                        INFLUX_USER, INFLUX_PASSWORD,
                        INFLUX_DBNAME)

req_obj = GenericRequests()
res_obj = ClientResponse()


class IseStorageInfo(APIView):
    '''Get total , available and used space of ise'''
    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting ISE Storage Information'''
        start_time = timeit.default_timer()
        ise_info = {}
        pool_list = []
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

            pool_response = req_obj.send_request(url_dynamic + RESOURCE['pools'], AUTH, headers=HEADER_JSON)

            if pool_response.get('message') == 'success':
                response_data = pool_response['result']['response']['data']['pools']

                if 'pools' in response_data:
                    pool_list.extend(response_data.get('pools', None))

                elif 'pool' in response_data:
                    pool_list.append(response_data.get('pool', None))

                ise_info['size'] = {
                    'total_size': 0,
                    'total_used': 0,
                    'total_available': 0,
                    'raid_available': {
                        'raid-0': 0,
                        'raid-1': 0,
                        'raid-5': 0
                    }
                }

                for pool in pool_list:
                    ise_info['size']['total_size'] = ise_info['size']['total_size'] + int(pool['size'])
                    ise_info['size']['total_used'] = ise_info['size']['total_used'] + int(pool['used']['_attr']['total'])
                    ise_info['size']['total_available'] = ise_info['size']['total_available'] \
                                                          + int(pool['available']['_attr']['total'])
                    ise_info['size']['raid_available']['raid-0'] = ise_info['size']['raid_available']['raid-0'] \
                                                                   + int(pool['available']['byredundancy']['raid-0'])
                    ise_info['size']['raid_available']['raid-1'] = ise_info['size']['raid_available']['raid-1'] \
                                                                   + int(pool['available']['byredundancy']['raid-1'])
                    ise_info['size']['raid_available']['raid-5'] = ise_info['size']['raid_available']['raid-5'] \
                                                                   + int(pool['available']['byredundancy']['raid-5'])

                (response, pool_status) = res_obj.response_formation(ise_info, status.HTTP_200_OK)
                total_time = timeit.default_timer() - start_time
                process_time = total_time - self.cortex_total
                if response.has_key('time_taken'):
                    response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                    response['time_taken']['python'] = "%.2fs"%process_time
                    response['time_taken']['total'] = "%.2fs"%total_time
                    response['time_taken']['req_recv_time'] = "%d"%int(start_time)
                    response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                return Response(response, status=pool_status)
            else:
                (response, pool_status) = res_obj.client_response(pool_response, time_res=True)
                return Response(response, pool_status)

class IseCardInfo(APIView):
    '''To get ise volume, host and wwn count'''
    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting ISE Card Info details'''
        start_time = timeit.default_timer()
        ise_info = {}

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
            response = req_obj.send_request(url_dynamic, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start

            if response.get('message') == 'success':
                data = response['result']['response']['data']['arrays']
                ise_info['serial_no'] = data['array']['globalid']
                ise_info['status'] = data['array']['status']
                ise_info['name'] = data['array']['name']
                ise_info['ipaddress1'] = data['array']['ipaddress1']
                ise_info['ipaddress2'] = data['array']['ipaddress2']
                controller_data = data['array']['controllers']
                if controller_data.has_key('controllers'):
                    ise_info['mrc1_status'] = controller_data['controllers'][0]['status']['_attr']['value']
                    ise_info['mrc2_status'] = controller_data['controllers'][1]['status']['_attr']['value']
                else:
                    if int(controller_data['controller']['_attr']['self'][-1]) == 1:
                        ise_info['mrc1_status'] = controller_data['controller']['status']['_attr']['value'] 
                        ise_info['mrc2_status'] = None 
                    else:
                        ise_info['mrc1_status'] = None 
                        ise_info['mrc2_status'] = controller_data['controller']['status']['_attr']['value'] 
                
                ise_info['led'] = data['array']['led']

                if 'hosts' in data['array']['hosts']:
                    ise_info['hosts'] = len(data['array']['hosts']['hosts'])

                elif 'host' in data['array']['hosts']:
                    ise_info['hosts'] = 1

                if 'volumes' in data['array']['volumes']:
                    ise_info['volumes'] = len(data['array']['volumes']['volumes'])

                elif 'volume' in data['array']['volumes']:
                    ise_info['volumes'] = 1

                if 'endpoints' in data['array']['endpoints']:
                    ise_info['endpoints'] = len(data['array']['endpoints']['endpoints'])

                elif 'endpoint' in data['array']['endpoints']:
                    ise_info['endpoints'] = 1

                if 'pools' in data['array']['pools']:
                    ise_info['pool'] = len(data['array']['pools']['pools'])

                elif 'pool' in data['array']['pools']:
                    ise_info['pool'] = 1

            self.cortex_start = timeit.default_timer()      
            mrc_response = req_obj.send_request(url_dynamic+'controllers', AUTH, headers=HEADER_JSON)
            self.cortex_total = self.cortex_total + (timeit.default_timer() - self.cortex_start)

            if mrc_response.get('message') == 'success':
                mrc_data = mrc_response['result']['response']['data']['controllers']
                if mrc_data.has_key('controllers'):
                    ise_info['mrc1_fwversion'] = mrc_data['controllers'][0]['fwversion']
                    ise_info['mrc2_fwversion'] = mrc_data['controllers'][1]['fwversion']
                else:
                    pass

            self.cortex_start = timeit.default_timer()    
            encrypt_response = req_obj.send_request(url_dynamic+'encryption', AUTH, headers=HEADER_JSON)
            self.cortex_total = self.cortex_total + (timeit.default_timer() - self.cortex_start)

            if encrypt_response.get('message') == 'success':
                encrypt_data = encrypt_response['result']['response']['data']['encryption']
                ise_info['encrpytion_enabled'] = encrypt_data['enabled']
                ise_info['locked'] = encrypt_data['locked']
                ise_info['eula'] = encrypt_data['eula']

            self.cortex_start = timeit.default_timer()
            query_url = dynamic_url(ise_id, query=True)
            url_dynamic_query = query_url[0]
            query_response = req_obj.send_request(url_dynamic_query, AUTH, headers=HEADER_JSON)
            self.cortex_total = self.cortex_total + (timeit.default_timer() - self.cortex_start)

            if query_response.get('message') == 'success':
                query_data = query_response['result']['response']['data']['array']['chronometer']['_attr']
                ise_info['time'] = query_data.get('time')
                ise_info['date'] = query_data.get('date')
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, card_status) = res_obj.response_formation(ise_info, status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total

            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs"%process_time
                response['time_taken']['python'] = "%.2fs"%self.cortex_total
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            return Response(response, status=card_status)

class IseInfo(APIView):
    '''To get ISE Info Details'''
    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting ISE Info details based on it's iseid'''
        start_time = timeit.default_timer()
        ise_info = {}

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
            res = req_obj.send_request(url_dynamic, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs"%process_time
                response['time_taken']['python'] = "%.2fs"%self.cortex_total
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            return Response(response, status=status_code)


class IseHardwareInfo(APIView):
    '''To get ISE Hardware Info details'''
    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting IseHardware info details'''
        start_time = timeit.default_timer()
        ise_info = {}
        get_url = dynamic_url(ise_id)
        cortex_one = 0.0
        cortex_two = 0.0
        cortex_three = 0.0
        cortex_four = 0.0
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            cortex_start_one = timeit.default_timer()
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            response = req_obj.send_request(url_dynamic, AUTH, headers=HEADER_JSON)
            cortex_one = timeit.default_timer() - cortex_start_one

            if response.get('message') == 'success':
                data = response['result']['response']['data']['arrays']['array']
                controller_data = data['controllers']
                if controller_data.has_key('controllers'):
                    ise_info['mrc'] = {
                        'mrc1': {'value': controller_data['controllers'][0]['status']['_attr']['value']},
                        'mrc2': {'value': controller_data['controllers'][1]['status']['_attr']['value']}
                    }
                else:
                    if int(controller_data['controller']['_attr']['self'][-1]) == 1:
                        ise_info['mrc'] = {
                            'mrc1': {'value': controller_data['controller']['status']['_attr']['value']},
                            'mrc2': {'value': None}
                        }
                    else:
                        ise_info['mrc'] = {
                            'mrc1': {'value': None},
                            'mrc2': {'value': controller_data['controller']['status']['_attr']['value']}
                        }

                if 'batteries' in data['batteries']:
                    ise_info['battery'] = {
                        'battery1': data['batteries']['batteries'][0]['status']['_attr'],
                        'battery2': data['batteries']['batteries'][1]['status']['_attr']
                    }
                elif 'battery' in data['batteries']:
                    ise_info['battery'] = {
                        'battery1': data['batteries']['battery']['status']['_attr']
                    }
                ise_info['uptime'] = []
                
                if 'led' in data['led']:
                    ise_info['led'] = {
                        'led' : data['led']['_attr']['string']
                    }

                if ise_info['mrc']['mrc1']['value'] == '0':
                    cortex_start_two = timeit.default_timer()
                    mrc1_url = "https://" + data['ipaddress1'] + "/storage/arrays/" + data['globalid']
                    mrc1_response = req_obj.send_request(mrc1_url + '/chronometer', AUTH, headers=HEADER_JSON)
                    cortex_two = timeit.default_timer() - cortex_start_two

                    if 'uptime' in mrc1_response['result']['response']['data']['chronometer']:
                        ise_info['uptime'].append({
                            'mrc1_uptime': mrc1_response['result']['response']['data']['chronometer']['uptime']
                        })

                if ise_info['mrc']['mrc2']['value'] == '0':
                    cortex_start_three = timeit.default_timer()
                    mrc2_url = "https://" + data['ipaddress2'] + "/storage/arrays/" + data['globalid']
                    mrc2_response = req_obj.send_request(mrc2_url + '/chronometer', AUTH, headers=HEADER_JSON)
                    cortex_three = timeit.default_timer() - cortex_start_three

                    if 'uptime' in mrc2_response['result']['response']['data']['chronometer']:
                        ise_info['uptime'].append({
                            'mrc2_uptime': mrc2_response['result']['response']['data']['chronometer']['uptime']
                        })

            media_response = req_obj.send_request((url_dynamic + 'media'), AUTH, headers=HEADER_JSON)

            if media_response.get('message') == 'success':
                media_data = media_response['result']['response']['data']['media']

                if 'media' in media_data:
                    ise_info['datapac'] = {
                        'datapac1': media_data['media'][0]['status']['details']['_attr'],
                        'datapac2': media_data['media'][1]['status']['details']['_attr'],
                    }

                if 'medium' in media_data:
                    if media_data['medium']['id'] == 1:
                        ise_info['datapac'] = {
                            'datapac1': media_data['medium']['status']['details']['_attr'],
                            'datapac2': {'value': '0x40000000'}
                        }

                    if media_data['medium']['id'] == 2:
                        ise_info['datapac'] = {
                            'datapac1': {'value': '0x40000000'},
                            'datapac2': media_data['medium']['status']['details']['_attr']
                        }
            cortex_start_four = timeit.default_timer()
            ps_response = req_obj.send_request(url_dynamic + '/powersupplies', AUTH, headers=HEADER_JSON)
            cortex_four = timeit.default_timer() - cortex_start_four

            if ps_response.get('message') == 'success':
                ps_data = ps_response['result']['response']['data']['powersupplies']
                if 'powersupplies' in ps_data:
                    ise_info['powersupply'] = {
                        'ps1': ps_data['powersupplies'][0]['status']['_attr'],
                        'ps2': ps_data['powersupplies'][1]['status']['_attr']
                    }
                    try:
                        ise_info['blowersps1'] = {
                            'ps1': ps_data['powersupplies'][0]['fans'][0]['status']['_attr'],
                            'ps2': ps_data['powersupplies'][0]['fans'][1]['status']['_attr']
                        }

                        ise_info['blowersps2'] = {
                            'ps1': ps_data['powersupplies'][1]['fans'][0]['status']['_attr'],
                            'ps2': ps_data['powersupplies'][1]['fans'][1]['status']['_attr']
                        }
                    except:
                        ise_info['blowersps1'] = {}
                        ise_info['blowersps2'] = {}

            alert = ['Volume 05 (Storage 01)', 'Volume 01 (Storage 01)', 'Volume 03 (Storage 01)', 'Volume 07 (Storage 01)',
                     'Volume 06 (Storage 01)', 'Volume 02 (Storage 01)', 'Volume 04 (Storage 01)', 'Volume 08 (Storage 01)']
            ise_info['alert'] = [random.choice(alert) for x in range(3)]
            ise_info['iops'] = [random.choice(alert) for x in range(3)]

            (response, hardware_status) = res_obj.response_formation(ise_info, status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            self.cortex_total = cortex_one + cortex_two + cortex_three +cortex_four
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                response['time_taken']['python'] = "%.2fs"%process_time
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
            return Response(response, status=hardware_status)

class ArrayIopsChart(APIView):
    '''To get array iops chart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting Array Iops Chart Details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readiops'] = '#ff7f0e'
        column_list['writeiops'] = '#2ca02c'
        column_list['totaliops'] = '#7777ff'
        metric_data = fetch_array_data(column_list, id)

        for data in metric_data:
            if data.get('key') == 'readiops':
                data['key'] = ARRAYCHART['readiops']
            elif data.get('key') == 'writeiops':
                data['key'] = ARRAYCHART['writeiops']
            else:
                data['key'] = ARRAYCHART['totaliops']
        
        (response, chart_status) = res_obj.response_formation(metric_data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=chart_status)


class ArrayDataRateChart(APIView):
    '''To get Array DataRate chart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting Array DataRate Chart Details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readkbps'] = '#ff7f0e'
        column_list['writekbps'] = '#2ca02c'
        column_list['totalkbps'] = '#7777ff'
        metric_data = fetch_array_data(column_list, id)

        for data in metric_data:
            if data.get('key') == 'readkbps':
                data['key'] = ARRAYCHART['readkbps']
            elif data.get('key') == 'writekbps':
                data['key'] = ARRAYCHART['writekbps']
            else:
                data['key'] = ARRAYCHART['totalkbps']
        
        (response, chart_status) = res_obj.response_formation(metric_data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=chart_status)


class ArrayQueueDepthChart(APIView):
    '''To get Array QueueDepth chart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting Array QueueDepth Chart Details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['queuedepth'] = '#ff7f0e'
        metric_data = fetch_array_data(column_list, id)

        for data in metric_data:
            if data.get('key') == 'queuedepth':
                data['key'] = ARRAYCHART['queuedepth']

        (response, chart_status) = res_obj.response_formation(metric_data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=chart_status)


class ArrayLatencyChart(APIView):
    '''To get Array Latency chart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting Array Latency Chart Details'''
        authorize = check_authorization(id)
        if authorize:
            (response, status_code) = res_obj.response_formation('Unauthorized', status.HTTP_401_UNAUTHORIZED)
            return Response(response, status=status_code)
        start_time = timeit.default_timer()
        column_list = collections.OrderedDict()
        column_list['readlatency'] = '#ff7f0e'
        column_list['writelatency'] = '#2ca02c'
        metric_data = fetch_array_data(column_list, id)

        for data in metric_data:
            if data.get('key') == 'readlatency':
                data['key'] = ARRAYCHART['readlatency']
            else:
                data['key'] = ARRAYCHART['writelatency']

        (response, chart_status) = res_obj.response_formation(metric_data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=chart_status)


def fetch_array_data(column_list, id):
    '''This is for fetching array data from influxdb based on it's id'''

    ise_obj = ListIse.objects.get(id=id)
    if ise_obj.mrc1_status:
        response = req_obj.send_request(('http://%s/query'% ise_obj.ip_primary), '',headers=HEADER_JSON)
    elif ise_obj.mrc2_status:
        response = req_obj.send_request(('http://%s/query'% ise_obj.ip_secondary), '',headers=HEADER_JSON)
    else:
        pass

    try:
        data = response['result']['response']['data']['array']['chronometer']
        date_time_str = str(data['_attr']['date']) + ' ' + str(data['_attr']['time'])
        curr_time = int(datetime.strptime(date_time_str, '%d-%b-%Y %H:%M:%S').strftime("%s"))
        end_time = curr_time - 24 * 60 * 60
        query = """SELECT time, %s
                      FROM arrays
                      WHERE global_id='%s' and  time  < %ss and time > %ss
                      """ % (','.join(column_list), ise_obj.serial_no, curr_time, end_time)
        result = client.query(query)
        metric_data = []
        counter =0
        for key, color in column_list.iteritems():
            metric_data.append({'key': key, 'color': color, 'values': []})
            for array_data in result:
                for data in array_data:
                    metric_data[counter]['values'].append({'x': data['time'], 'y': data[key]})
            counter = counter + 1
        return metric_data
    except:
        pass

def check_authorization(id):
    '''This is for checking authorization'''
    get_url = dynamic_url(id)
    url_dynamic = get_url[0]
    AUTH = get_url[1]
    res = req_obj.send_request(url_dynamic, AUTH, headers=HEADER_JSON)
    (response, status_code) = res_obj.client_response(res)
    if response['message'] == 'fail':
        if response['result']['error']['status_code'] == 401:
            return res

class ArrayDedupChart(APIView):
    '''To get Array Dedup Chart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting array dedup chart details'''
        start_time = timeit.default_timer()

        ise_obj = ListIse.objects.get(id=id)

        query = "select count, refcnt from dedup where global_id='%s' and time > now() - 24h"%ise_obj.serial_no
        result = client.query(query)
        metric_data = []
        dedup_data = {'key': 'dedup', 'color': '#7777ff', 'values': []}

        for array_dedup_data in result:
            for data in array_dedup_data:
                dedup_data['values'].append({'x': data['refcnt'], 'y': data['count']})
        metric_data.append(dedup_data)
        (response, chart_status) = res_obj.response_formation(metric_data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=chart_status)

class IseHosts(APIView):
    '''To get Host list based on it's id'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting Ise Host list based on it's id'''
        start_time = timeit.default_timer()
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            result = []
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic+RESOURCE['hosts']
            self.cortex_start = timeit.default_timer()
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            if res['message'] == 'success':
                host_list = []
                result = []
                host_data = res['result']['response']['data']
                if host_data.has_key('hosts'):
                    if host_data['hosts'].has_key('host'):
                        host_list.append(host_data['hosts']['host'])
                    elif host_data['hosts'].has_key('hosts'):
                        host_list.extend(host_data['hosts']['hosts'])
                    else:
                        res['result']['response']['data']['hosts']['hosts'] = []
                else:
                    res['result']['response']['data']['hosts']['hosts'] = []

                for host in host_list:
                    result.append({'ise_id':int(ise_id),'hosts': host['name'], 'host_id': host['id']})

                res['result']['response']['data']['hosts']['hosts'] = result
                (response,status_code) = res_obj.client_response(res, time_res=True)
                response['result']['response']['data']['hosts']['ise_id'] = int(ise_id)
                total_time = timeit.default_timer() - start_time
                process_time = total_time - self.cortex_total
                if 'time_taken' in response:
                    response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                    response['time_taken']['python'] = "%.2fs"%process_time
                    response['time_taken']['total'] = "%.2fs"%total_time
                    response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                    response['time_taken']['req_recv_time'] = "%d"%int(start_time)
                return Response(response, status_code)

            else:
                (response,status_code) = res_obj.client_response(res)
                return Response(response, status=status_code)
