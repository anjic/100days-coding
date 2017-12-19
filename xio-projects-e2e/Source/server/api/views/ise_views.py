from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import json
import ast
import urllib
import os
import timeit
import subprocess
import time

# other library
from xio_ise.settings import BASE_DIR
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from utility.dynamic_url_formation import (dynamic_url, network_ip_select)
from utility.encryption import encryption, decryption
from api.models.sangroup_models import SanGroup
from api.models.ise_models import (ListIse, SangroupIse)
from api.serializer.ise_serializer import IseListSerializer
from config import (AUTH, HEADER_JSON,
                    ISE_STATUS_CODE, RESOURCE,
                    ISE_STATUS)
req_obj = GenericRequests()
res_obj = ClientResponse()


class IseList(APIView):
    '''List all Arrays, or create Node Attribute'''

    def get(self, request, format=None):
        '''This is for getting list of all ises'''
        start_time = timeit.default_timer()
        ise = ListIse.objects.all()
        iseserializer = IseListSerializer(ise, many=True)

        for ise_id in iseserializer.data:
            san_ise = SangroupIse.objects.values('sg_id').filter(ise_id=ise_id['id'])
            list_sg = SanGroup.objects.values('sangroup_name', 'sangroup_id', 'comment').filter(sangroup_id__in=san_ise)
            ise_id['sangroup'] = [data for data in list_sg]
        (response, status_code) = res_obj.response_formation(iseserializer.data, status.HTTP_200_OK, time_res=True)
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
        ''' This is for creating new ise and mapping with related sangroup'''
        ip_primary_add = None
        ip_secondary_add = None

        ise_primary_ip = ListIse.objects.filter(
            Q(ip_primary=request.data['array']['controllers']['controllers'][0]['ipaddress']) | Q(
                ip_primary=request.data['array']['controllers']['controllers'][1]['ipaddress']))

        for ise in ise_primary_ip:
            ip_primary_add = ise.ip_primary

        if ip_primary_add:
            (response, status_code) = res_obj.response_formation('Primary IP Already Exists', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)

        ise_secondary_ip = ListIse.objects.filter(
            Q(ip_secondary=request.data['array']['controllers']['controllers'][1]['ipaddress']) | Q(
                ip_secondary=request.data['array']['controllers']['controllers'][0]['ipaddress']))

        for ise in ise_secondary_ip:
            ip_secondary_add = ise.ip_secondary

        if ip_secondary_add:
            (response, status_code) = res_obj.response_formation('Secondary IP Already Exists', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)

        try:
            id_list = []
            data = request.data['array']
            root_id = None
            ise = ListIse()
            ise_list = ListIse.objects.filter(prefered=1)
            if ise_list:
                id_list = [ise_id.id for ise_id in ise_list]

            if request.data['ise_name']:
                ise.ise_name = request.data['ise_name']
            else:
                ise.ise_name = 'ISE-' + request.data['array']['serialnumber']

            ise.raw_data = json.dumps(request.data['string_data'])
            ise.root_node_id = root_id
            ise.serial_no = request.data['array']['serialnumber']
            ise.ip_primary = request.data['array']['controllers']['controllers'][0]['ipaddress']
            if ise.ip_primary is not None:
                primary_url = "https://" + str(ise.ip_primary) + "/query"
                res = req_obj.send_request(
                    primary_url, None, headers=HEADER_JSON)

                if res['message'] == 'success':
                    ise.mrc1_status = True
                else:
                    ise.mrc1_status = False
            else:
                ise.mrc1_status = False

            serial_no = request.data['array']['serialnumber']
            url = "https://" + str(ise.ip_primary) + \
                "/storage/arrays/" + serial_no
            contact_info = {}
            contact_info['contactphone'] = request.data.get('contactphone')
            contact_info['contactemail'] = request.data.get('contactemail')
            contact_info['contactname'] = request.data.get('contactname')
            contact_info['location'] = request.data.get('location')
            contact_info['address'] = request.data.get('address')
            res = req_obj.send_request(
                url,
                AUTH,
                headers=HEADER_JSON,
                data=contact_info,
                method='PUT')
            if res['message'] == 'success':
                ise.contactphone = request.data.get('contactphone')
                ise.contactemail = request.data.get('contactemail')
                ise.contactname = request.data.get('contactname')
                ise.location = request.data.get('location')
                ise.address = request.data.get('address')

            if request.data['array']['controllers']['controllers'][1]['ipaddress']:
                ise.ip_secondary = request.data['array']['controllers']['controllers'][1]['ipaddress']

            if ise.ip_secondary is not None:
                secondary_url = "https://" + str(ise.ip_secondary) + "/query"
                res = req_obj.send_request(
                    secondary_url, None, headers=HEADER_JSON)
                if res['message'] == 'success':
                    ise.mrc2_status = True
                else:
                    ise.mrc2_status = False
            else:
                ise.mrc2_status = False

            ise.username = request.data['user_name']
            if request.data['prefered_ise']:
                ListIse.objects.filter(id__in=id_list).update(prefered=False)
                ise.prefered = True if request.data['prefered_ise'] else False
            ise.password = encryption(request.data['user_password'])
            ise.save()
            ise_id = ise.id

            if request.data.get('sangroup_name'):
                san_group = SanGroup()
                san_group.sangroup_name = request.data['sangroup_name']
                san_group.comment = request.data['comment']
                san_group.save()

                sangroup = SangroupIse()
                san = SanGroup.objects.get(
                    sangroup_name=request.data['sangroup_name'])
                sangroup.ise_id = ise_id
                sangroup.sg_id = san.sangroup_id
                sangroup.save()

            for san_id in request.data['sangroup_id']:
                san = SangroupIse()
                san.ise_id = ise_id
                san.sg_id = san_id
                san.save()
            subprocess.Popen("python %s severity_update" %
                             (os.path.join(BASE_DIR, 'manage.py')), shell=True)
            (response, status_code) = res_obj.response_formation('ISE Added Successfully', status.HTTP_201_CREATED)
            return Response(response, status=status_code)
        except Exception as e:
            (response, status_code) = res_obj.response_formation(str(e), status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)


class IseDetail(APIView):
    '''Retrieve,Update or Delete a ise instance'''

    def get_object(self, id):
        '''This is for getting particular object for ise'''
        try:
            return ListIse.objects.get(id=id)
        except ListIse.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        '''This is for getting particular Ise based on it's id'''
        start_time = timeit.default_timer()
        query_url = dynamic_url(id, query=True)
        if query_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('ISE Not Reachable', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        url_dynamic_query = query_url[0]
        AUTH = query_url[1]
        ise = self.get_object(id)
        serializer = IseListSerializer(ise)
        str_data = json.loads(serializer.data['raw_data'])
        obj_data = ast.literal_eval(json.dumps(str_data))
        query_response = req_obj.send_request(
            url_dynamic_query, AUTH, headers=HEADER_JSON)
        if query_response['message'] != 'success':
            (response, status_code) = res_obj.response_formation(
                'ISE Not Reachable', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        controller_data = query_response['result']['response']['data']['array']['controllers']
        controllers = []
        if 'controllers' in controller_data:
            for i in range(len(controller_data)):
                i = {
                    "fwversion": controller_data['controllers'][i]['fwversion'],
                    "macaddress": controller_data['controllers'][i]['macaddress'],
                    "ipaddress": controller_data['controllers'][i]['ipaddress']}
                controllers.append(i)
        elif 'controller' in controller_data:
            controller = {
                "fwversion": controller_data['controller']['fwversion'],
                "macaddress": controller_data['controller']['macaddress'],
                "ipaddress": controller_data['controller']['ipaddress']
            }
            controllers.append(controller)
        else:
            pass

        ise_details = {}
        ise_details['model'] = query_response['result']['response']['data']['array']['model']
        ise_details['controllers'] = {}
        ise_details['controllers']['controllers'] = controllers

        for key, data in serializer.data.iteritems():
            ise_details[key] = data
        ise_details['raw_data'] = obj_data
        (response, status_code) = res_obj.response_formation(ise_details, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)


class IseSanMap(APIView):
    ''' Map sangroup with multiple ise  '''

    def get(self, request, id, format=None):
        '''get all ise list with selected sangroup'''
        start_time = timeit.default_timer()
        ise_list = ListIse.objects.values('id', 'ise_name', 'ip_primary', 'ip_secondary')
        for ise in ise_list:
            san = SangroupIse.objects.all().filter(Q(sg_id=id) & Q(ise_id=ise['id']))
            if san:
                ise['checked'] = True
            else:
                ise['checked'] = False
        (response, status_code) = res_obj.response_formation(ise_list, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)

    def put(self, request, id, format=None):
        ''' This is for mapping ise with multiple sangroup  '''
        response = {}
        for ise_id in request.data['added']:
            san = SangroupIse()
            san.ise_id = ise_id
            san.sg_id = id
            san.save()

        for ise_id in request.data['removed']:
            san = SangroupIse.objects.filter(
                Q(sg_id=id) & Q(ise_id=ise_id)).delete()

        (response, status_code) = res_obj.response_formation('Mapping Done Successfully', status.HTTP_200_OK)
        return Response(response, status=status_code)


class SanIseMap(APIView):
    '''Map sangroup for selected ise'''

    def get(self, request, id, format=None):
        '''This is for getting sangroup list for selected ise'''
        start_time = timeit.default_timer()
        san_list = SanGroup.objects.values('sangroup_id', 'sangroup_name')
        for san in san_list:
            ise = SangroupIse.objects.all().filter(Q(sg_id=san['sangroup_id']) & Q(ise_id=id))
            if ise:
                san['checked'] = True
            else:
                san['checked'] = False
        (response, status_code) = res_obj.response_formation(san_list, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)

    def put(self, request, id, format=None):
        ''' This is for mapping sangroup with selected ise  '''
        for san_id in request.data['added']:
            san = SangroupIse()
            san.ise_id = id
            san.sg_id = san_id
            san.save()

        for san_id in request.data['removed']:
            san = SangroupIse.objects.filter(Q(sg_id=san_id) & Q(ise_id=id)).delete()

        (response, status_code) = res_obj.response_formation('Mapping Done Successfully', status.HTTP_200_OK)
        return Response(response, status=status_code)


class IseManagement(APIView):
    '''Update and change ISE name, username and password'''

    def put(self, request, id, format=None):
        '''This is for updating ISE details and password'''
        req_data = request.data.get('data')
        get_url = dynamic_url(id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            iselist = ListIse.objects.values(
                'username',
                'password',
                'ise_name').get(id=id)

            if 'new_password' in request.data:
                password = {}
                ise = ListIse.objects.values('username', 'password').get(id=id)
                if decryption(
                        ise['password']) == request.data['curr_password']:
                    password['password'] = request.data['new_password']
                    url = url_dynamic+'users/'+ise['username']
                    res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=password, method='PUT')
                    Auth = (AUTH[0], str(request.data['new_password']))
                    res = req_obj.send_request(url, Auth, headers=HEADER_JSON)
                    if res.get('message') == 'success':
                        ise = ListIse.objects.get(id=id)
                        ise.password = encryption(request.data['new_password'])
                        ise.save()
                        (response, status_code) = res_obj.response_formation('Password Changed Successfully', status.HTTP_200_OK)
                        return Response(response, status=status_code)
                else:
                    (response, status_code) = res_obj.response_formation('Current Password Wrong', status.HTTP_400_BAD_REQUEST)
                    return Response(response, status=status_code)

            if 'password' in request.data:
                Auth = (AUTH[0], str(request.data['password']))
                ise = ListIse.objects.get(id=id)
                url = url_dynamic+'users/'+ise.username
                res = req_obj.send_request(url, Auth, headers=HEADER_JSON)
                if res.get('message') == 'success':
                    ise.password = encryption(request.data['password'])
                    ise.save()
                    (response, status_code) = res_obj.response_formation('Password Changed Successfully',
                                                                            status.HTTP_200_OK)
                    return Response(response, status=status_code)
                else:
                    (response, status_code) = res_obj.response_formation('Password is invalid',
                                                                         status.HTTP_400_BAD_REQUEST)
                    return Response(response, status=status_code)

            if req_data:
                ise = ListIse.objects.get(id=id)

                if ('name' in req_data or 'contactname' in req_data or 'contactphone' in req_data or 'contactemail' in req_data or 'location' in req_data or req_data.get('address')):
                    query_string = urllib.urlencode(req_data)
                    url = url_dynamic[:-1]
                    res = req_obj.send_request(
                        url, AUTH, headers=HEADER_JSON, data=query_string, method='PUT')
                    if res.get('message') == 'success':
                        ise = ListIse.objects.get(id=id)
                        if req_data.get('name'):
                            ise.ise_name = req_data.get('name')
                        else:
                            pass
                        if 'contactname' in req_data:
                            ise.contactname = req_data.get('contactname')
                        else:
                            pass
                        if 'contactphone' in req_data:
                            ise.contactphone = req_data.get('contactphone')
                        else:
                            pass
                        if 'contactemail' in req_data:
                            ise.contactemail = req_data.get('contactemail')
                        else:
                            pass
                        if 'location' in req_data:
                            ise.location = req_data.get('location')
                        else:
                            pass
                        if 'address' in req_data:
                            ise.address = req_data.get('address')
                        else:
                            pass
                    ise.save()

                if 'prefered_ise' in req_data:
                    ise_list = ListIse.objects.filter(prefered=1)
                    id_list = [ise_id.id for ise_id in ise_list]
                    ListIse.objects.filter(
                        id__in=id_list).update(
                        prefered=False)
                    ise.prefered = req_data.get('prefered_ise')
                    ise.save()
                else:
                    pass
            (response, status_code) = res_obj.response_formation({'ise_name': iselist.get('ise_name'), 'success_message': 'Updated Successfully'}, status.HTTP_200_OK)
            return Response(response, status=status_code)

    def delete(self, request, id, format=None):
        '''This is for deleting particular ise based on its id'''
        san = SangroupIse.objects.filter(ise_id=id)
        if san:
            (response, status_code) = res_obj.response_formation('ISE Present in one or more SAN Group', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)
        else:
            ise = ListIse.objects.filter(id=id).delete()
            (response, status_code) = res_obj.response_formation({'delete_message': 'ISE Removed Successfully'}, status.HTTP_200_OK)
            return Response(response, status=status_code)


class AdvancedSettings(APIView):
    '''Perform ise advance settings like Restart, initialize and shutdown'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting ISE advance setting status like Restart,initialize and shutdown'''
        start_time = timeit.default_timer()
        ise_obj = ListIse.objects.values(
            'ip_primary',
            'ip_secondary').get(id=id)
        get_url = dynamic_url(id)
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
            string = res['result']['response']['data']['arrays']['array']['status']['_attr']['string']
            primary_url = "https://" + str(ise_obj['ip_primary']) + "/query"
            ping1_response = os.system(
                "ping -c 1 " + str(ise_obj['ip_primary']))
            ping2_response = os.system(
                "ping -c 1 " + str(ise_obj['ip_secondary']))

            if ping1_response == 0 or ping2_response == 0:
                get_ise = ListIse.objects.get(id=id)
                if string == 'Uninitialized':
                    get_ise.status = ISE_STATUS_CODE['reformat']
                    get_ise.save()
                else:
                    get_ise.status = ISE_STATUS_CODE['running']
                    get_ise.save()

            ise_status = ListIse.objects.values('status').get(id=id)
            for message, code in ISE_STATUS_CODE.iteritems():
                if code == ise_status['status']:
                    ISE_STATUS[message] = True
                else:
                    ISE_STATUS[message] = False
            (response, status_code) = res_obj.response_formation(
                ISE_STATUS, status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            process_time = total_time - self.cortex_total
            if 'time_taken' in response:
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(timeit.default_timer())
            return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        '''This is for performing ise advance settings like Restart, initialize and shutdown'''
        get_url = dynamic_url(id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            url_dynamic = get_url[0][:-1]
            AUTH = get_url[1]

            ise_obj = ListIse.objects.get(id=id)

            if request.data['restart']:
                request.data['restart'] = 'true'
                query_string = urllib.urlencode(request.data)
                res = req_obj.send_request(url_dynamic,
                                           AUTH,
                                           headers=HEADER_JSON,
                                           data=query_string,
                                           method='PUT')
                if res['result']['status_code'] == 504:
                    ise_obj.status = ISE_STATUS_CODE['restart']
                    ise_obj.save()
                    ISE_STATUS['restart'] = True
                    (response, status_code) = res_obj.response_formation(ISE_STATUS, status.HTTP_200_OK)
                    return Response(response, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

            elif request.data['initialize']:
                ise_obj.initialize = "started"
                ise_obj.save()
                request.data['initialize'] = 'true'
                query_string = urllib.urlencode(request.data)
                ise_obj.initialize = "running"
                ise_obj.save()
                res = req_obj.send_request(url_dynamic,
                                           AUTH,
                                           headers=HEADER_JSON,
                                           data=query_string,
                                           method='PUT')
                ise_obj.status = ISE_STATUS_CODE['initialize']
                ise_obj.initialize = "finished"
                ISE_STATUS['initialize'] = True
                ise_obj.save()
                (response, status_code) = res_obj.response_formation(ISE_STATUS, status.HTTP_200_OK)
                return Response(response, status=status.HTTP_202_ACCEPTED)

            elif request.data['reformat']:
                request.data['reformat'] = 'true'
                query_string = urllib.urlencode(request.data)
                res = req_obj.send_request(url_dynamic,
                                           AUTH,
                                           headers=HEADER_JSON,
                                           data=query_string,
                                           method='PUT')
                if res['result']['status_code'] == 504:
                    ise_obj.status = ISE_STATUS_CODE['reformat']
                    ise_obj.save()
                    ISE_STATUS['reformat'] = True
                    (response, status_code) = res_obj.response_formation(ISE_STATUS, status.HTTP_200_OK)
                    return Response(response, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

            elif request.data['shutdown']:
                request.data['shutdown'] = 'true'
                query_string = urllib.urlencode(request.data)
                res = req_obj.send_request(url_dynamic,
                                           AUTH,
                                           headers=HEADER_JSON,
                                           data=query_string,
                                           method='PUT')
                request.data['shutdown'] = 'true'
                query_string = urllib.urlencode(request.data)
                res = req_obj.send_request(url_dynamic,
                                           AUTH,
                                           headers=HEADER_JSON,
                                           data=query_string,
                                           method='PUT')
                if res['result']['status_code'] == 504:
                    ise_obj.status = ISE_STATUS_CODE['shutdown']
                    ise_obj.save()
                    ISE_STATUS['shutdown'] = True
                    (response, status_code) = res_obj.response_formation(ISE_STATUS, status.HTTP_200_OK)
                    return Response(response, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


class IseStatus(APIView):
    '''To get ise status for particular ise based on its id'''

    def __init__(self):
        '''This initializes the instances of the class'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, id, format=None):
        '''This is for getting ise status based on its id'''
        start_time = timeit.default_timer()
        get_url = dynamic_url(id)

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
            url = url_dynamic
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            if res["message"] == "success":
                try:
                    ise_status = {}
                    ise_status['status'] = res['result']['response']['data']['arrays']['array']['status']
                    ise_status['globalid'] = res['result']['response']['data']['arrays']['array']['globalid']
                    res['result']['response']['data']['arrays']['array'] = ise_status
                    (response, status_code) = res_obj.client_response(res)
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
                except BaseException:
                    pass
            else:
                (response, status_code) = res_obj.client_response(res, time_res=True)
                return Response(response, status=status_code)


class IseLed(APIView):
    '''Update particular ise led based on its id'''

    def __init__(self):
        '''This initiates the instance of the class'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, id):
        '''This is an object for getting ise-details'''
        start_time = timeit.default_timer()
        get_url = dynamic_url(id)
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
                response['time_taken']['cortex'] = "%.2fs" % self.cortex_total
                response['time_taken']['python'] = "%.2fs" % process_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
            return Response(response, status=status_code)

    def get(self, request, id, format=None):
        '''This is getting ise-details based on its id'''
        return self.get_object(id)

    def put(self, request, id, format=None):
        '''Update particular volume based on it's id'''
        get_url = dynamic_url(id)
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
            url = url_dynamic[:-1]
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)


class IseInitialize(APIView):
    '''Get ISE initialization status'''

    def get_object(self, id):
        '''This is an object for getting ise initialization status'''
        start_time = timeit.default_timer()
        total_time = 0
        ise_obj = ListIse.objects.get(id=id)
        ise_initialize = {}
        ise_initialize['initialize'] = ise_obj.initialize
        (response, status_code) = res_obj.response_formation(ise_initialize, status.HTTP_200_OK, time_res=True)
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d" % int(start_time)
        return Response(response, status=status_code)

    def get(self, request, id, format=None):
        '''This is for getting ise initialization status'''
        return self.get_object(id)


class IseIpUpdate(APIView):
    '''Update IP address manually if ip_primary and ip_secondary in down state'''

    def get(self, request, ise_id, format=None):
        ''' This is for getting ise details for given ise id'''
        ise = ListIse.objects.get(id=ise_id)
        if ise:
            start_time = timeit.default_timer()
            ise_details = {}
            ise_details['ise_id'] = ise_id
            ise_details['ise_name'] = ise.ise_name
            ise_details['ise_serialno'] = ise.serial_no
            ise_details['ip_primary'] = ise.ip_primary
            ise_details['ip_secondary'] = ise.ip_secondary
            (response, status_code) = res_obj.response_formation(ise_details, status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            if 'time_taken' in response:
                response['time_taken']['cortex'] = "0.0s"
                response['time_taken']['python'] = "%.2fs" % total_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
        else:
            (response, status_code) = res_obj.response_formation("ISE Not Found", status.HTTP_404_NOT_FOUND)
        return Response(response, status=status_code)

    def put(self, request, ise_id, format=None):
        ''' This is for checking given ip address is valid and updated in DB '''

        ip = request.data.get('modify_ip', None)
        get_url = network_ip_select(ise_id, manual_ip=ip)

        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            ise = ListIse.objects.get(id=ise_id)

            if ip == ise.ip_primary or ip == ise.ip_secondary:
                (response, status_code) = res_obj.response_formation('Given IP already exists in %s' % ise.ise_name, status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)

            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['network']
            res = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            ise_Name_db = ise.ise_name if ise else None

            if res['message'] == 'success':
                ise_Name_cortex = res['result']['response']['data']['array']['name']

                if ise_Name_db == ise_Name_cortex:
                    controller_data = res['result']['response']['data']['array']['controllers']['controllers']
                    ise.ip_primary = controller_data[0]['ipaddress']
                    ise.ip_secondary = controller_data[1]['ipaddress']
                    ise.save()
                    (response, status_code) = res_obj.response_formation(
                        'Updated new IP successfully', status.HTTP_200_OK)
                    return Response(response, status=status_code)
                (response, status_code) = res_obj.response_formation('IP already exists in different ISE', status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)
            (response, status_code) = res_obj.response_formation('IP not reachable', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)
