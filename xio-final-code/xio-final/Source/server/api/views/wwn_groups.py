from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib
import timeit
import copy
from django.db.models import Q
import gevent

from utility.dynamic_url_formation import dynamic_url
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE)
from api.models.ise_models import (ListIse, SangroupIse)
from api.models.servermgmt_models import (ServerWwnIse, ServerMgmt)
req_obj = GenericRequests()
res_obj = ClientResponse()

class WWNGroupList(APIView):
    """To get all Hosts"""
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def common(self,request_details = {}):

        ises = []

        response = req_obj.send_request(request_details.get('url'), request_details.get('auth'), headers=HEADER_JSON)
        wwn_ise = {}
        wwn_ise['ise_id'] = request_details.get('ise_id')
        wwn_ise['ise_name'] = request_details.get('ise_name')
        wwn_ise['ise_serialno'] = request_details.get('ise_serialno')
        wwn_ise['wwn'] = []
        if response.get('message') == 'success':
            # wwn_ise['wwn_array'] = []

            endpoint_res = response['result']['response']['data']['endpoints']
            if endpoint_res.has_key('endpoint'):
                if endpoint_res['endpoint']['host'] == "" and endpoint_res['endpoint']['array'] == "":
                    wwn_ise['wwn'].append(endpoint_res['endpoint']['globalid'])
                # if endpoint_res['endpoint']['_attr']['type'] == 'array':
                #     wwn_ise['wwn_array'].append(endpoint_res['endpoint']['globalid'])

            elif endpoint_res.has_key('endpoints'):
                for endpoints in endpoint_res['endpoints']: 
                    if endpoints['host'] == "" and endpoints['array'] == "":
                        wwn_ise['wwn'].append(endpoints['globalid'])
                    # if endpoints['_attr']['type'] == 'array': 
                    #     wwn_ise['wwn_array'].append(endpoints['globalid'])
            else:
                pass
            ises.append(wwn_ise.copy())

        return ises


    def get(self, request, ise_id, format=None):

        ise_id_list = ise_id.split(',')
        result = {}
        result['common'] = {}
        result['un_common'] = []

        ise_list = []
        for ise in ise_id_list:
            ise_list.append(ListIse.objects.get(id=ise))
        threads = []
        for i, ise in enumerate(ise_list):
            get_url = dynamic_url(ise.id)

            if get_url == status.HTTP_404_NOT_FOUND:
                continue
               
            elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                continue
                
            else:
                urls_details = {
                    'url': get_url[0]+RESOURCE['endpoints'],
                    'auth': get_url[1],
                    'ise_id': ise.id,
                    'ise_name':ise.ise_name,
                    'ise_serialno':ise.serial_no
                }
                threads.append(gevent.spawn(self.common, request_details=urls_details))
        end_result = gevent.joinall(threads)

        for thread in threads:
            result['un_common'].extend(thread.value)

        if len(result['un_common']) > 1:
            result['common']['ise_id'] = ise_id_list
            result['common']['ise_name'] = []
            result['common']['ise_serialno'] = []
            common = set(result.get('un_common')[0]['wwn'])

            for res in result.get('un_common'):
                common = common & set(res['wwn'])
                result['common']['ise_serialno'].append(res['ise_serialno'])
                result['common']['ise_name'].append(res['ise_name'])

            result['common']['wwn'] = list(common)

            for uncommon in result['un_common']:
                uncommon['wwn'] = list(set(uncommon['wwn']) - set(result['common']['wwn']))
        else:
            result['common']['ise_id'] = [result['un_common'][0]['ise_id']]
            result['common']['ise_name'] = [result['un_common'][0]['ise_name']]
            result['common']['ise_serialno'] = [result['un_common'][0]['ise_serialno']]
            result['common']['wwn'] = result['un_common'][0]['wwn']
            result['un_common'] = []

        (response, status_code) = res_obj.response_formation(result,
                                                             status.HTTP_200_OK)
        return Response(response, status=status_code)


class WWNGroupCreate(APIView):
    """
    """
    # pass
    def get(self, request, server_id, format=None):
        """
        """
        result = {}
        ise_list = ListIse.objects.all()
        ser_mgmt = ServerMgmt.objects.get(server_id=server_id)
        if ser_mgmt:
            result['server'] = {}
            result['server']['server_name'] = ser_mgmt.server_name
            result['server']['server_id'] = ser_mgmt.server_id
            result['ises'] = []
            threads = []

            for i, ise in enumerate(ise_list):
                get_url = dynamic_url(ise.id)

                if get_url == status.HTTP_404_NOT_FOUND:
                    continue
                   
                elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                    continue
                    
                else:
                    urls_details = {
                        'url': get_url[0]+RESOURCE['hosts'],
                        'auth': get_url[1],
                        'ise_id': ise.id,
                        'ise_name':ise.ise_name,
                        'ise_serialno':ise.serial_no
                    }
                    threads.append(gevent.spawn(get_wwn_ise, request_details=urls_details))
            end_result = gevent.joinall(threads)

            for thread in threads:
                result['ises'].extend(thread.value)

            # result['ises'] = get_wwn_ise(ise_list)
            (response, status_code) = res_obj.response_formation(result,status.HTTP_200_OK)
            return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.response_formation("Server Not Found",status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)


    def post(self, request, server_id, format=None):
        """
        payload = {
            "name":"wwngroup01",
            "comment":"wwngroup01",
            "wwns":[
                {
                "ise_id":5,
                "wwn":"2001010101010000"
                },
                {
                "ise_id":5,
                "wwn":"2001010101010001"
                },
                {
                "ise_id":6,
                "wwn":"2001010101010002"
                },
                {
                "ise_id":6,
                "wwn":"2001010101010003"
                }
            ]
            }  
        """
        payload = request.data
        result = {}
        wwns = []
        wwn_response = []
        for wwn in payload.get('wwns'):
            try:
                result[wwn.get('ise_id')].append(wwn.get('wwn'))
            except:
                result[wwn.get('ise_id')] = [wwn.get('wwn')]

        for key, value in result.iteritems():
            wwns.append({'ise_id': key, 'endpoint': value})
        payload['wwns'] = wwns

        for wwn in payload['wwns']:
            wwn['name'] = payload.get('wwn_name')
            wwn['comment'] = payload.get('comment')

        for wwn_id in payload['wwns']:
            ise_id = wwn_id['ise_id']
            get_url = dynamic_url(ise_id)
            del wwn_id['ise_id']

            if get_url == status.HTTP_404_NOT_FOUND:
                (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
                return Response(response, status=status_code)
            elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
                return Response(response, status=status_code)
            else:
                url_dynamic = get_url[0]
                AUTH = get_url[1]
                url = url_dynamic+RESOURCE['hosts']
                query_string = urllib.urlencode(wwn_id,doseq=True)
                res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='POST')

                if res.get('message') != 'success':
                    wwn_response.append(res.copy())
                else:
                    server_san = ServerWwnIse()
                    server_san.server_id = ServerMgmt.objects.get(server_id = server_id )
                    server_san.ise_id = ListIse.objects.get(id=ise_id)
                    server_san.wwngroup = wwn_id['name']
                    server_san.save()

        if wwn_response:
            (response, status_code) = res_obj.response_formation("WWN Group not created", status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation("WWN Group created successfully", status.HTTP_200_OK)
        return Response(response, status=status_code)

def get_wwn_ise(request_details={}):

    ises = []
    wwn_ise = {}
    res = req_obj.send_request(request_details.get('url'), request_details.get('auth'), headers=HEADER_JSON)
    wwn_ise['ise_id'] = request_details.get('ise_id')
    wwn_ise['ise_name'] = request_details.get('ise_name')
    wwn_ise['ise_serialno'] = request_details.get('ise_serialno')
    wwn_ise['wwns'] = []
    ise_id = request_details.get('ise_id')
    if res['message'] == 'success':
        wwngroup = []
        host_res = res['result']['response']['data']['hosts']
        if host_res.has_key('host'):
            server_wwn = ServerWwnIse.objects.filter(ise_id_id=ise_id,wwngroup=host_res['host']['name'])
            if server_wwn:
                for server in server_wwn:
                    ser_name = server.server_id.server_name
                wwngroup.append(host_res['host']['name'])
                wwn = {}
                wwn['wwngroup'] = wwngroup
                wwn['wwngroup_id'] = host_res['host']['id']
                wwn['server_name'] = ser_name
            else:
                wwn = {}
                wwn['wwngroup'] = host_res['host']['name']
                wwn['wwngroup_id'] = host_res['host']['id']
                wwn['server_name'] = ''
            wwn_ise['wwns'].append(wwn)

        elif host_res.has_key('hosts'):
            for hosts in host_res['hosts']:
                server_wwn = ServerWwnIse.objects.filter(ise_id_id=ise_id,wwngroup=hosts['name'])
                if server_wwn:
                    for server in server_wwn:
                        ser_name = server.server_id.server_name
                        wwn = {}
                        wwn['wwngroup'] = server.wwngroup
                        wwn['server_name'] = ser_name
                        wwn['wwngroup_id'] = hosts['id']
                else:
                    wwn = {}
                    wwn['wwngroup'] = hosts['name']
                    wwn['wwngroup_id'] = hosts['id']
                    wwn['server_name'] = ''

                wwn_ise['wwns'].append(wwn)
        else:
            pass
    ises.append(wwn_ise.copy())

    return ises

class WWNGroupDetail(APIView):
    """Retrieve,Update or Delete a wwngroup instance"""
    def get_object(self, ise_id, wwngroup_id, san_id):
        """To get particular object"""
        get_url = dynamic_url(ise_id)
        if get_url == status.HTTP_404_NOT_FOUND:
            (response, status_code) = res_obj.response_formation('ISE Not Found', status.HTTP_404_NOT_FOUND)
            return Response(response, status=status_code)

        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            (response, status_code) = res_obj.response_formation('Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)

        else:
            ise_list = []
            if san_id:
                san_ise = SangroupIse.objects.filter(sg_id = san_id)
                for ise in san_ise:
                    ise_list.append(ise.ise_id)
            else:
                ises = ListIse.objects.all()
                for ise in ises:
                    ise_list.append(ise.id)
            ise = ListIse.objects.get(id=ise_id)
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic+RESOURCE['hosts']+"/"+wwngroup_id
            url_wwn = url_dynamic+RESOURCE['endpoints']
            response  = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            response_wwn  = req_obj.send_request(url_wwn, AUTH, headers=HEADER_JSON)
            res = {}
            res['ises'] = ise_list
            res['ise_details'] = {}
            res['ise_details']['ise_id'] = ise_id
            res['ise_details']['ise_name'] = ise.ise_name
            res['ise_details']['ise_serialno'] = ise.serial_no
            res['wwn'] = {}
            res['wwn']['wwngroup_id'] = wwngroup_id
            res['wwn']['current_wwn'] = []
            res['wwn']['available_wwn'] = []
            if response.get('message') == 'success':
                host_res = response['result']['response']['data']['hosts']['host']
                res['wwn']['wwngroup_name'] = host_res['name']
                if host_res['endpoints'].has_key('endpoint'):
                    res['wwn']['current_wwn'].append(host_res['endpoints']['endpoint']['globalid'])
                if host_res['endpoints'].has_key('endpoints'):
                    for endpoint in host_res['endpoints']['endpoints']:
                        res['wwn']['current_wwn'].append(endpoint['globalid'])

                endpoint_res = response_wwn['result']['response']['data']['endpoints']
                if endpoint_res.has_key('endpoint'):
                    if endpoint_res['endpoint']['host'] == "" and endpoint_res['endpoint']['array'] == "":
                        res['wwn']['available_wwn'].append(endpoint_res['endpoint']['globalid'])

                elif endpoint_res.has_key('endpoints'):
                    for endpoints in endpoint_res['endpoints']:
                        if endpoints['host'] == "" and endpoints['array'] == "":
                            res['wwn']['available_wwn'].append(endpoints['globalid'])
                else:
                    pass
            (response, status_code) = res_obj.response_formation(res,status.HTTP_200_OK)    
            return Response(response, status=status_code)

    def get(self, request, ise_id, wwngroup_id, san_id, format=None):
        """Get particular wwngroup based on it's id"""
        return self.get_object(ise_id,wwngroup_id,san_id)

    def put(self, request, ise_id, wwngroup_id, san_id, format=None):
        """Update particular wwngroup based on it's id
        """
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
            remove_endpoint_result = []
            client_data = dict(request.data)
  
            payload = client_data
            url = url_dynamic+RESOURCE['hosts']+"/"+wwngroup_id
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=payload, method='PUT')
            if res['result']['status_code'] == 201:
                if client_data.get('removed_endpoint'):
                    remove_endpoint = client_data.get('removed_endpoint', [])
                    del client_data['removed_endpoint']
                    for i in remove_endpoint:
                        endpoint_url = url_dynamic+'endpoints/'+str(i)
                        endpoint_res = req_obj.send_request(endpoint_url, AUTH, headers=HEADER_JSON)
                        host_id = endpoint_res['result']['response']['data']['endpoints']['endpoint']['host']['globalid']
                        url = url_dynamic + RESOURCE['hosts'] + "/" + str(host_id)
                        endpoint_remove_url = url+'?endpoint='+str(i)
                        del_res  = req_obj.send_request(endpoint_remove_url, AUTH, headers=HEADER_JSON, method='DELETE')
                        remove_endpoint_result.append(del_res.get('result', ''))
                    res['result']['response']['removed_endpoint_res'] = remove_endpoint_result
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

class WWNGroupUpdate(APIView):

    def put(self, request, server_id, format=None):
        ''' mapping wwn with ise  '''
        server_mgmt = ServerMgmt.objects.get(server_id = server_id)
        ser_name = server_mgmt.server_name
        if request.data['server_name'] != ser_name:
            server_mgmt.server_name = request.data.get('server_name')
            server_mgmt.save()
        for data in request.data['added']:
            server_wwn = ServerWwnIse()
            server_wwn.ise_id = ListIse.objects.get(id=data.get('ise_id'))
            server_wwn.server_id = ServerMgmt.objects.get(server_id = server_id )
            server_wwn.wwngroup = data.get('wwngroup')
            server_wwn.save()

        for server in request.data['removed']:
            server_wwn = ServerWwnIse.objects.filter(Q(server_id_id=server_id) & Q(wwngroup=server.get('wwngroup'))).delete()

        (response, status_code) = res_obj.response_formation('Mapping Done Successfully',
                                                             status.HTTP_200_OK)
        return Response(response, status=status_code)

class WWNGroupServer(APIView):

    def get(self, request, san_id, server_id, format=None):
        """
        """
        result = {}
        san_ise = SangroupIse.objects.filter(sg_id=san_id)
        ser_mgmt = ServerMgmt.objects.get(server_id=server_id)
        result['server'] = {}
        result['server']['server_name'] = ser_mgmt.server_name
        result['server']['server_id'] = ser_mgmt.server_id
        result['ises'] = []
        ises = []
        for ise in san_ise:
            ises.append(ise.ise_id)

        ise_list = []
        for ise in ises:
            ise_list.append(ListIse.objects.get(id=ise))
        threads = []

        for i, ise in enumerate(ise_list):
            get_url = dynamic_url(ise.id)

            if get_url == status.HTTP_404_NOT_FOUND:
                continue
               
            elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                continue
                
            else:
                urls_details = {
                    'url': get_url[0]+RESOURCE['hosts'],
                    'auth': get_url[1],
                    'ise_id': ise.id,
                    'ise_name':ise.ise_name,
                    'ise_serialno':ise.serial_no
                }
                threads.append(gevent.spawn(get_wwn_ise, request_details=urls_details))
        end_result = gevent.joinall(threads)

        for thread in threads:
            result['ises'].extend(thread.value)

        (response, status_code) = res_obj.response_formation(result,status.HTTP_200_OK)
        return Response(response, status=status_code)