from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import timeit

from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from api.models.sangroup_models import SanGroup
from api.models.ise_models import SangroupIse, ListIse
from api.serializer.sangroup_serializer import SanGroupSerializer
from utility.dynamic_url_formation import dynamic_url
from config import (AUTH, HEADER_JSON, RESOURCE)

req_obj = GenericRequests()
res_obj = ClientResponse()


class SanGroupList(APIView):
    '''List all SanGroup, or create SanGroup'''

    def get(self, request, format=None):
        '''This is for getting a list of all sangroup'''
        start_time = timeit.default_timer()
        sangroups = SanGroup.objects.all()
        serializer = SanGroupSerializer(sangroups, many=True)

        for sg_id in serializer.data:
            san_ise = SangroupIse.objects.values(
                'ise_id').filter(sg_id=sg_id['sangroup_id'])
            list_ise = ListIse.objects.values(
                'ise_name', 'id').filter(
                id__in=san_ise)
            sg_id['ise'] = [data for data in list_ise]
        (response, status_code) = res_obj.response_formation(
            serializer.data, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time

        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)

    def post(self, request, format=None):
        '''This is for creating new sangroup'''
        serializer = SanGroupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            (response, status_code) = res_obj.response_formation(
                serializer.data, status.HTTP_201_CREATED)
            return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation(
            serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status_code)


class SanGroupDetail(APIView):
    '''Retrieve,Update or Delete a SanGroup instance'''

    def __init__(self):
        '''To create instance of the class'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, id):
        '''This is for getting particular object'''
        try:
            return SanGroup.objects.get(sangroup_id=id)
        except SanGroup.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''This is for getting particular SanGroup based on it's id'''
        start_time = timeit.default_timer()
        sangroup = self.get_object(id)
        serializer = SanGroupSerializer(sangroup)
        sg_details = {}

        for k, v in serializer.data.iteritems():
            sg_details[k] = v
        san_ise = SangroupIse.objects.values('ise_id').filter(
            sg_id=serializer.data['sangroup_id'])
        list_ise = ListIse.objects.values(
            'ise_name',
            'id',
            'raw_data',
            'serial_no',
            'ip_primary',
            'ip_secondary',
            'time_stamp').filter(
            id__in=san_ise)
        sg_details['ise'] = [data for data in list_ise]

        for ise in sg_details['ise']:
            get_url = dynamic_url(ise['id'])

            if get_url == status.HTTP_404_NOT_FOUND:
                continue
            elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                continue
            else:
                self.cortex_start = timeit.default_timer()
                url_dynamic = get_url[0]
                AUTH = get_url[1]
                response = req_obj.send_request(
                    url_dynamic, AUTH, headers=HEADER_JSON)
                self.cortex_total = self.cortex_total + \
                    (timeit.default_timer() - self.cortex_start)

                if response.get('message') == 'success':
                    data = response['result']['response']['data']['arrays']

                    if 'hosts' in data['array']['hosts']:
                        ise['hosts'] = len(data['array']['hosts']['hosts'])
                    elif 'host' in data['array']['hosts']:
                        ise['hosts'] = 1

                    if 'volumes' in data['array']['volumes']:
                        ise['volumes'] = len(
                            data['array']['volumes']['volumes'])
                    elif 'volume' in data['array']['volumes']:
                        ise['volumes'] = 1

                    if 'endpoints' in data['array']['endpoints']:
                        ise['endpoints'] = len(
                            data['array']['endpoints']['endpoints'])
                    elif 'endpoint' in data['array']['endpoints']:
                        ise['endpoints'] = 1

                    if 'pools' in data['array']['pools']:
                        ise['pools'] = len(data['array']['pools']['pools'])
                    elif 'pool' in data['array']['pools']:
                        ise['pools'] = 1

                    self.cortex_start = timeit.default_timer()
                    pool_response = req_obj.send_request(
                        url_dynamic + '/pools', AUTH, headers=HEADER_JSON)
                    response_data = pool_response['result']['response']['data']['pools']
                    self.cortex_total = self.cortex_total + \
                        (timeit.default_timer() - self.cortex_start)

                    pool_list = []
                    if 'pools' in response_data:
                        pool_list.extend(response_data['pools'])

                    elif 'pool' in response_data:
                        pool_list.append(response_data['pool'])

                    ise['size'] = {
                        'total_size': 0,
                        'total_used': 0,
                        'available': 0
                    }

                    for pool in pool_list:
                        ise['size']['total_size'] = ise['size']['total_size'] + \
                            int(pool['size'])
                        ise['size']['total_used'] = ise['size']['total_used'] + \
                            int(pool['used']['_attr']['total'])
                        ise['size']['available'] = ise['size']['available'] + \
                            int(pool['available']['_attr']['total'])

        (response, status_code) = res_obj.response_formation(
            sg_details, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total

        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
            response['time_taken']['python'] = "%.2fs" % process_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)

    def put(self, request, id, format=None):
        '''This is for updating particular sangroup based on it's id'''
        sangroup = self.get_object(id)
        serializer = SanGroupSerializer(sangroup, data=request.data)

        if serializer.is_valid():
            serializer.save()
            (response, status_code) = res_obj.response_formation(
                serializer.data, status.HTTP_200_OK)
            return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation(
            serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status_code)

    def delete(self, request, id, format=None):
        '''This is for deleting particular sangroup based on it's id if not present in any ise'''
        san = SangroupIse.objects.filter(sg_id=id)

        if san:
            (response, status_code) = res_obj.response_formation(
                'SAN Group Mapped with one or more ISE', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)
        else:
            sangroup = self.get_object(id)
            sangroup.delete()
            sangroups = SanGroup.objects.all()
            serializer = SanGroupSerializer(sangroups, many=True)

            for sg_id in serializer.data:
                san_ise = SangroupIse.objects.values(
                    'ise_id').filter(sg_id=sg_id['sangroup_id'])
                list_ise = ListIse.objects.values(
                    'ise_name', 'id').filter(
                    id__in=san_ise)
                sg_id['ise'] = [data for data in list_ise]
                sg_id['hosts'] = []

                for ise in list_ise:
                    get_url = dynamic_url(ise['id'])

                    if get_url == status.HTTP_404_NOT_FOUND:
                        continue
                    elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                        continue
                    else:
                        url_dynamic = get_url[0]
                        AUTH = get_url[1]
                        url = url_dynamic + RESOURCE['hosts']
                        res = req_obj.send_request(
                            url, AUTH, headers=HEADER_JSON)

                        if res['message'] == 'success':
                            host_data = res['result']['response']['data']['hosts']
                            host_list = []

                            if 'hosts' in host_data:
                                host_list.extend(host_data['hosts'])
                            elif 'host' in host_data:
                                host_list.append(host_data['host'])

                            for host in host_list:
                                sg_id['hosts'].append(
                                    {'ise_id': ise['id'], 'hosts': host['name'], 'host_id': host['id']})
            (response, status_code) = res_obj.response_formation(
                {'san_list': serializer.data, 'deleted_san': sangroup.sangroup_name}, status.HTTP_200_OK)
            return Response(response, status=status_code)


class SanGroupHost(APIView):
    '''Retrieve All Host list for SanGroup instance'''

    def __init__(self):
        '''To create an instance for the class'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, id):
        '''This is for getting particular object'''
        try:
            return SanGroup.objects.get(sangroup_id=id)
        except SanGroup.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''This is for getting Host list based on sangroup'''
        start_time = timeit.default_timer()
        sangroup_host_list = []
        sangroup = self.get_object(id)
        serializer = SanGroupSerializer(sangroup)
        san_ise = SangroupIse.objects.values('ise_id').filter(
            sg_id=serializer.data['sangroup_id'])
        list_ise = ListIse.objects.values(
            'id', 'ise_name').filter(
            id__in=san_ise)

        for ise_list in list_ise:
            get_url = dynamic_url(ise_list['id'])

            if get_url == status.HTTP_404_NOT_FOUND:
                continue
            elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                continue
            else:
                self.cortex_start = timeit.default_timer()
                url_dynamic = get_url[0]
                AUTH = get_url[1]
                url = url_dynamic + RESOURCE['hosts']
                res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
                self.cortex_total = timeit.default_timer() - self.cortex_start
                (response, status_code) = res_obj.client_response(res, time_res=True)

                if status_code == 200:
                    if 'hosts' in response['result']['response']['data']['hosts']:
                        hosts = [host for host in response['result']
                                 ['response']['data']['hosts']['hosts']]

                        for data in hosts:
                            host_list = {}
                            host_list['ise_id'] = ise_list['id']
                            host_list['ise_name'] = ise_list['ise_name']
                            host_list['id'] = data['id']
                            host_list['name'] = data['name']
                            host_list['host_comment'] = data['comment']
                            sangroup_host_list.append(host_list)

                    elif 'host' in response['result']['response']['data']['hosts']:
                        hosts = response['result']['response']['data']['hosts']['host']
                        host_list = {}
                        host_list['ise_id'] = ise_list['id']
                        host_list['ise_name'] = ise_list['ise_name']
                        host_list['id'] = hosts['id']
                        host_list['name'] = hosts['name']
                        host_list['host_comment'] = hosts['comment']
                        sangroup_host_list.append(host_list)
        (response, status_code) = res_obj.response_formation(
            sangroup_host_list, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total

        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
            response['time_taken']['python'] = "%.2fs" % process_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)


class SanIseDetail(APIView):
    '''Retrieve,Update or Delete a SanGroup instance'''

    def __init__(self):
        '''To create an instance for the class'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for getting particular SanGroup/ise details'''
        start_time = timeit.default_timer()
        sg_details = {}
        sg_details['ise'] = []
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
            ise = ListIse.objects.values(
                'ise_name',
                'id',
                'raw_data',
                'serial_no',
                'ip_primary',
                'ip_secondary',
                'time_stamp').get(
                id=ise_id)

            url_dynamic = get_url[0]
            AUTH = get_url[1]
            response = req_obj.send_request(
                url_dynamic, AUTH, headers=HEADER_JSON)
            self.cortex_total = self.cortex_total + \
                (timeit.default_timer() - self.cortex_start)

            if response.get('message') == 'success':
                data = response['result']['response']['data']['arrays']

                if 'hosts' in data['array']['hosts']:
                    ise['hosts'] = len(data['array']['hosts']['hosts'])
                elif 'host' in data['array']['hosts']:
                    ise['hosts'] = 1

                if 'volumes' in data['array']['volumes']:
                    ise['volumes'] = len(data['array']['volumes']['volumes'])
                elif 'volume' in data['array']['volumes']:
                    ise['volumes'] = 1

                if 'endpoints' in data['array']['endpoints']:
                    ise['endpoints'] = len(
                        data['array']['endpoints']['endpoints'])
                elif 'endpoint' in data['array']['endpoints']:
                    ise['endpoints'] = 1

                if 'pools' in data['array']['pools']:
                    ise['pools'] = len(data['array']['pools']['pools'])
                elif 'pool' in data['array']['pools']:
                    ise['pools'] = 1
                ise['status'] = data['array']['status']['_attr']['string']
                self.cortex_start = timeit.default_timer()
                pool_response = req_obj.send_request(
                    url_dynamic + '/pools', AUTH, headers=HEADER_JSON)
                response_data = pool_response['result']['response']['data']['pools']
                self.cortex_total = self.cortex_total + \
                    (timeit.default_timer() - self.cortex_start)

                pool_list = []
                if 'pools' in response_data:
                    pool_list.extend(response_data['pools'])

                elif 'pool' in response_data:
                    pool_list.append(response_data['pool'])

                ise['size'] = {
                    'total_size': 0,
                    'total_used': 0,
                    'available': 0
                }

                for pool in pool_list:
                    ise['size']['total_size'] = ise['size']['total_size'] + \
                        int(pool['size'])
                    ise['size']['total_used'] = ise['size']['total_used'] + \
                        int(pool['used']['_attr']['total'])
                    ise['size']['available'] = ise['size']['available'] + \
                        int(pool['available']['_attr']['total'])

            sg_details = [ise]

        (response, status_code) = res_obj.response_formation(
            sg_details, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total

        if 'time_taken' in response:
            response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
            response['time_taken']['python'] = "%.2fs" % process_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)
