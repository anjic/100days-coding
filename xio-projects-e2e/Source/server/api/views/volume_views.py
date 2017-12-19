from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib
import time
import re
import timeit
import copy

# other library
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from utility.dynamic_url_formation import dynamic_url
from config import (AUTH, HEADER_JSON, RESOURCE)

req_obj = GenericRequests()
res_obj = ClientResponse()


class VolumesList(APIView):
    '''To get all volumes based on ise id'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting volume list'''
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
            url = url_dynamic + RESOURCE['volumes']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            if response.get('message') == 'success':
                vol_res = response['result']['response']['data']['volumes']

                if 'volume' in vol_res:
                    vol_res['volume']['ise_id'] = ise_id
                    vol_res['volume']['volume_id'] = vol_res['volume']['id']
                    if 'allocation' in vol_res['volume']['allocations']:
                        vol_res['volume']['allocation'] = [
                            vol_res['volume']['allocations']['allocation']]
                    else:
                        if vol_res['volume']['allocations']['allocations']:
                            vol_res['volume']['allocation'] = vol_res['volume']['allocations']['allocations']
                        else:
                            vol_res['volume']['allocation'] = []

                elif 'volumes' in vol_res:
                    for volumes in vol_res['volumes']:
                        volumes['ise_id'] = ise_id
                        volumes['volume_id'] = volumes['id']
                        if 'allocation' in volumes['allocations']:
                            volumes['allocation'] = [
                                volumes['allocations']['allocation']]
                        else:
                            volumes['host_id'] = volumes['id']
                            volumes['ise_id'] = ise_id
                            for i in range(len(vol_res['volumes'])):
                                if 'allocations' in volumes['allocations']:
                                    if volumes['allocations']['allocations']:
                                        volumes['allocation'] = volumes['allocations']['allocations']
                                    else:
                                        volumes['allocation'] = []

                                else:
                                    volumes['allocation'] = [
                                        volumes['allocations']['allocation']]
                else:
                    pass

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

    def post(self, request, ise_id, format=None):
        '''This is for creating new volumes'''
        request_data = request.data
        volume_name = request_data['name']
        host_names = request_data['host_list']
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
            url = url_dynamic + RESOURCE['volumes']
            url_pools = url_dynamic + RESOURCE['pools']
            get_res_pools = req_obj.send_request(
                url_pools, AUTH, headers=HEADER_JSON)
            if request_data['create_like_volumes'] and request_data.get(
                    'alloctype') == 0 and request_data.get('dedup') == 0:
                if get_res_pools.get('message') == 'success':
                    get_pool_data = get_res_pools['result']['response']['data']['pools']
                    raid = 'raid-' + str(request_data.get('redundancy'))
                    free_size = None
                    if 'pool' in get_pool_data:
                        free_capacity = get_pool_data['pool']['available']['byredundancy'].get(
                            raid)
                        free_size = free_capacity / \
                            (request_data['size'] * request_data['no_like_volumes'])
                    elif 'pools' in get_pool_data:
                        for pool in get_pool_data['pools']:
                            if request_data.get('pool') == pool.get('id'):
                                free_capacity = pool['available']['byredundancy'].get(
                                    raid)
                                free_size = free_capacity / \
                                    (request_data['size'] * request_data['no_like_volumes'])
                    else:
                        pass
                    if free_size == 0:
                        (response, status_code) = res_obj.response_formation(
                            'Not Enough Space For Creating Multiple Volumes', status.HTTP_400_BAD_REQUEST)
                        return Response(response, status=status_code)
            all_payload = {}
            query_string = urllib.urlencode(request.data, doseq=True)
            res = req_obj.send_request(url,AUTH,headers=HEADER_JSON,data=query_string,method='POST')

            if res['message'] == 'success':
                volume_res = res['result']['response']['data']
                volume_id = re.search(r'\((.*?)\)', volume_res).group(1)

                if volume_id:
                    allocation_url = url_dynamic + RESOURCE['allocations']
                    all_payload['volumename'] = volume_name

                else:
                    volume_guid = False
                    while volume_guid == False:
                        volume_response = req_obj.send_request(
                            url, AUTH, headers=HEADER_JSON)
                        volume_data = volume_response['result']['response']['data']['volumes']
                        if 'volume' in volume_data:
                            if volume_data['volume']['name'] == request.data['name']:
                                if volume_data['volume']['id']:
                                    volume_id = volume_data['volume']['id']
                                    volume_guid = True

                        elif 'volumes' in volume_data:
                            for volumes in volume_data['volumes']:
                                if volumes['name'] == request.data['name']:
                                    if volume_data['volume']['id']:
                                        volume_id = volume_data['volume']['id']
                                        volume_guid = True
                        else:
                            pass

                volume_get_url = url_dynamic + \
                    RESOURCE['volumes'] + '/' + volume_id
                vol_get_res = req_obj.send_request(volume_get_url, AUTH, headers=HEADER_JSON)
                volume_created = False

                while volume_created == False:
                    if vol_get_res['result']['status_code'] == 200:
                        if 'volume' in vol_get_res['result']['response']['data']['volumes']:
                            if vol_get_res['result']['response']['data']['volumes']['volume']['status']['_attr']['string'] == 'Operational':
                                volume_created = True
                                for host_name in host_names:
                                    if host_name['host']:
                                        all_payload['hostname'] = host_name['label']
                                        all_payload['lun'] = host_name['lun']
                                        allocation_res = req_obj.send_request(
                                            allocation_url, AUTH, headers=HEADER_JSON, data=all_payload, method='POST')
                                        if allocation_res.get(
                                                'message') == 'fail':
                                            (response, status_code) = res_obj.response_formation(
                                                allocation_res['result']['response']['data'], status.HTTP_400_BAD_REQUEST)
                                            return Response(
                                                response, status=status_code)
                            else:
                                vol_get_res = req_obj.send_request(volume_get_url, AUTH, headers=HEADER_JSON)
                        else:
                            vol_get_res = req_obj.send_request(volume_get_url, AUTH, headers=HEADER_JSON)
                    else:
                        vol_get_res = req_obj.send_request(volume_get_url, AUTH, headers=HEADER_JSON)

                if request.data['create_like_volumes']:
                    req_name = request_data['name']
                    for i in range(int(request.data['no_like_volumes'])):
                        request_data['name'] = req_name + \
                            "-" + str(i + 1).zfill(3)
                        query_string = urllib.urlencode(request_data, doseq=True)
                        res_like = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='POST')

                (response, status_code) = res_obj.response_formation(res['result']['response']['data'], status.HTTP_200_OK)
                return Response(response, status=status_code)

            else:
                (response, status_code) = res_obj.client_response(res)
                return Response(response, status=status_code)


class VolumeDetail(APIView):
    '''Retrieve,Update or Delete a volumes instance'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, ise_id, volume_id):
        '''This is for getting particular volume object'''
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
            url = url_dynamic + RESOURCE['volumes'] + "/" + volume_id
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

    def get(self, request, ise_id, volume_id, format=None):
        '''This is for getting particular volume based on it's id'''
        return self.get_object(ise_id, volume_id)

    def put(self, request, ise_id, volume_id, format=None):
        '''This is for updating particular volume based on it's id'''
        payload = dict(request.data)
        allocate_out = {}
        for key, value in payload.iteritems():
            if key == 'alloctype':
                allocate_out = {key: value}

        if allocate_out:
            payload.pop('alloctype')

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
            url = url_dynamic + RESOURCE['volumes'] + "/" + volume_id
            if allocate_out:
                res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=allocate_out, method='PUT')
                if res['message'] == 'fail':
                    (response, status_code) = res_obj.client_response(res)
                    return Response(response, status=status_code)
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

    def delete(self, request, volume_id, ise_id, format=None):
        '''This is for deleting particular volume based on it's id'''
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
            url = url_dynamic + RESOURCE['volumes'] + "/" + volume_id
            res = req_obj.send_request(
                url, AUTH, headers=HEADER_JSON, method='DELETE')
            if res['message'] == 'success':
                (response, status_code) = res_obj.response_formation(
                    {'deleted_volume': volume_id}, status.HTTP_200_OK)
                return Response(response, status=status_code)
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)


class Allocation(APIView):
    '''mapping volume with multiple hosts'''

    def put(self, request, ise_id, format=None):
        '''This is for allocating particular volume with multiple hosts'''
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
            req = dict(request.data)
            allocation_res = []
            host_url = url_dynamic + RESOURCE['hosts']

            if req.get('present'):
                pr_url = url_dynamic + RESOURCE['allocations']
                temp = {}
                temp['volumename'] = req['volume_name']
                for host_name in req['present']:
                    temp['hostname'] = host_name['host']
                    temp['lun'] = host_name['lun']
                    data_string = urllib.urlencode(temp)
                    pr_res = req_obj.send_request(
                        pr_url, AUTH, headers=HEADER_JSON, data=data_string, method='POST')
                    if pr_res.get('message') != 'success':
                        allocation_res.append(pr_res.copy())

            if req.get('unpresent'):
                allocationid = []
                for i in range(len(req.get('unpresent'))):
                    host_id = req.get('unpresent')[i]['hostid']
                    res = req_obj.send_request(
                        host_url, AUTH, headers=HEADER_JSON)
                    (response, status_code) = res_obj.client_response(res)

                    if response.get('message') == 'success':
                        host_res = response['result']['response']['data']['hosts']
                        if 'host' in host_res:
                            if host_res['host']['id'] == host_id:
                                if 'allocation' in host_res['host']['allocations']:
                                    if host_res['host']['allocations']['allocation']['volumename'] == request.data.get(
                                            'volume_name'):
                                        allocationid.append(
                                            host_res['host']['allocations']['allocation']['globalid'])
                                        break
                                if 'allocations' in host_res['host']['allocations']:
                                    for allocations in host_res['host']['allocations']['allocations']:
                                        if allocations['volumename'] == request.data.get(
                                                'volume_name'):
                                            allocationid.append(
                                                allocations['globalid'])
                                            break

                        elif 'hosts' in host_res:
                            for hosts in host_res['hosts']:
                                if hosts['id'] == host_id:
                                    if 'allocation' in hosts['allocations']:
                                        if hosts['allocations']['allocation']['volumename'] == request.data.get(
                                                'volume_name'):
                                            allocationid.append(
                                                hosts['allocations']['allocation']['globalid'])
                                            break

                                    if 'allocations' in hosts['allocations']:
                                        for allocations in hosts['allocations']['allocations']:
                                            if allocations['volumename'] == request.data.get(
                                                    'volume_name'):
                                                allocationid.append(
                                                    allocations['globalid'])
                                                break
                                    else:
                                        allocationid.append(
                                            hosts['allocations']['allocation']['globalid'])
                        else:
                            pass

                for all_id in allocationid:
                    upr_url = url_dynamic + \
                        RESOURCE['allocations'] + "/" + str(all_id)
                    upr_res = req_obj.send_request(
                        upr_url, AUTH, headers=HEADER_JSON, method='DELETE')
                    if upr_res.get(
                            'message') != 'success' and upr_res['result']['status_code'] != 404:
                        allocation_res.append(upr_res.copy())

            if req.get('changed'):
                temp = {}
                for change in req['changed']:
                    allocationid = change.get('globalID')
                    temp['lun'] = change.get('lun')
                    data_string = urllib.urlencode(temp)
                    modify_url = url_dynamic + \
                        RESOURCE['allocations'] + "/" + str(allocationid)
                    change_res = req_obj.send_request(
                        modify_url, AUTH, headers=HEADER_JSON, data=data_string, method='PUT')
                    if change_res.get('message') != 'success':
                        allocation_res.append(change_res.copy())

            if not allocation_res:
                (response, status_code) = res_obj.response_formation(
                    "Volume allocation updated successfully", status.HTTP_200_OK)
            else:
                (response, status_code) = res_obj.response_formation(
                    "Volume allocation failed", status.HTTP_400_BAD_REQUEST)

            return Response(response, status=status_code)


class VolumeChart(APIView):
    '''To get volumechart details'''

    def __init__(self):
        '''This initializes the class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting volume chart details'''
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
            url = url_dynamic + RESOURCE['volumes']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            if res['message'] == 'success':
                volume_total = {}
                volume_list = []
                data = res['result']['response']['data']
                if 'volumes' in data:
                    if 'volume' in data['volumes']:
                        volume_list.append(data['volumes']['volume'])
                    elif 'volumes' in data['volumes']:
                        volume_list.extend(data['volumes']['volumes'])
                    else:
                        res['result']['response']['data']['volumes']['volumes'] = []
                else:
                    res['result']['response']['data']['volumes']['volumes'] = []

                total_size = 0
                total_allocpercent = 0
                for volume in volume_list:
                    total_size = total_size + float(volume['size'])
                    total_allocpercent = total_allocpercent + \
                        (float(volume['allocpercent']) * float(volume['size']))
                volume_total = {
                    'overall_size': int(total_size),
                    'overall_allocpercent': int(total_allocpercent)
                }
                res['result']['response']['data'].pop('volumes')
                res['result']['response']['data'].update(volume_total)
                (response, status_code) = res_obj.client_response(
                    res, time_res=True)
                total_time = timeit.default_timer() - start_time
                process_time = total_time - self.cortex_total
                if 'time_taken' in response:
                    response['time_taken']['cortex'] = "%.2fs" % process_time
                    response['time_taken']['python'] = "%.2fs" % self.cortex_total
                    response['time_taken']['total'] = "%.2fs" % total_time
                    response['time_taken']['req_recv_time'] = "%d" % int(
                        start_time)
                    response['time_taken']['res_send_time'] = "%d" % int(
                        timeit.default_timer())
                return Response(response, status=status_code)
            else:
                (response, status_code) = res_obj.client_response(res)
                return Response(response, status=status_code)
