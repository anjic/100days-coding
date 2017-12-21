from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import timeit

# other library
from utility.dynamic_url_formation import dynamic_url, network_ip_select
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE)
from utility.network_ipaddress import ip_ping
from api.models.ise_models import ListIse

req_obj = GenericRequests()
res_obj = ClientResponse()


class NetworkList(APIView):
    '''To get and update Network details'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get(self, request, ise_id, format=None):
        '''This is for get Network details'''
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
            url = url_dynamic + RESOURCE['network']
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

    def put(self, request, ise_id, format=None):
        '''This is for update Network details'''
        primary_choice = True
        port_number = None
        network_data = {}
        ipaddress = 0

        if request.data['dhcp'] == 'enabled':
            return self.dhcp_enabled(ise_id, request.data)

        if 'network' in request.data:
            network_data = request.data['network']
            del request.data['network']
            dns_data = request.data
            two_response = ''
            set_status = status.HTTP_200_OK

            for port in range(2):
                if network_data.get(str(port), None):
                    port_number = port + 1
                    ip_data = network_data.get(str(port))
                    if ip_data.get('ipaddress', None):
                        ipaddress = ip_data['ipaddress']
                        primary_choice = True if port_number == 1 else False
                        get_url = network_ip_select(
                            ise_id, primary=primary_choice)
                    else:
                        get_url = dynamic_url(ise_id)
                    response_data = self.network_update(
                        ise_id=ise_id,
                        get_url=get_url,
                        dns_data=dns_data,
                        ip_data=ip_data,
                        ipaddress=ipaddress,
                        port_number=port_number)
                    ipaddress = 0
                    dns_data = {}
                    if response_data['status_code'] == '200':
                        two_response += 'Network %d Updated Successfully ' % port_number
                    elif response_data['status_code'] == '400':
                        two_response += 'Network %d given IP already exists ' % port_number
                        set_status = status.HTTP_400_BAD_REQUEST
                    elif response_data['status_code'] == '404':
                        two_response += response_data['result']
                        set_status = status.HTTP_404_NOT_FOUND
                    elif response_data['status_code'] == '504':
                        two_response += 'Connection Refused '
                        set_status = status.HTTP_504_GATEWAY_TIMEOUT
            (response, status_code) = res_obj.response_formation(
                two_response, set_status)
            return Response(response, status=status_code)

        get_url = dynamic_url(ise_id)
        response_data = self.network_update(
            ise_id=ise_id,
            get_url=get_url,
            dns_data=request.data,
            ip_data={},
            ipaddress=None,
            port_number=1)
        (
            res_data,
            set_status) = (
            'Connection Refused',
            status.HTTP_504_GATEWAY_TIMEOUT) if not response_data['message'] == 'success' else (
            'Network Updated Successfully',
            status.HTTP_200_OK)
        (response, status_code) = res_obj.response_formation(res_data, set_status)
        return Response(response, status=status_code)

    def dhcp_enabled(self, ise_id, dhcp_data={}):
        '''This is for dhcp enable mode'''
        ise = ListIse.objects.get(id=ise_id)
        ips = [ise.ip_secondary, ise.ip_primary]

        for ip in ips:
            ip_status = ip_ping(ip)
            primary_choice = True if ips.index(ip) == 0 else False

            if ip_status:
                get_url = network_ip_select(ise_id, primary=primary_choice)
                if get_url == status.HTTP_404_NOT_FOUND:
                    (response, status_code) = res_obj.response_formation(
                        'ISE Not Found', status.HTTP_404_NOT_FOUND)
                    return Response(response, status=status_code)
                elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                    (response, status_code) = res_obj.response_formation(
                        'Connection Refused', status.HTTP_504_GATEWAY_TIMEOUT)
                    return Response(response, status=status_code)
                else:
                    url_dynamic = get_url[0]
                    AUTH = get_url[1]
                    url = url_dynamic + RESOURCE['network']
                    response = req_obj.send_request(
                        url, AUTH, headers=HEADER_JSON, data=dhcp_data, method='PUT')

                    if response['message'] == 'success':
                        url = url_dynamic + RESOURCE['network']
                        response_get = req_obj.send_request(
                            url, AUTH, headers=HEADER_JSON)

                        if response_get['message'] == 'success':
                            get_ip = response_get['result']['response']['data']['network']['ports']['ports'][0]['ipaddress']
                            ise.ip_primary = get_ip
                            ise.save()
                            (response, status_code) = res_obj.response_formation(
                                'Network Updated Successfully', status.HTTP_200_OK)
                            return Response(response, status=status_code)
                    elif response['result']['status_code'] == 400:
                        (response, status_code) = res_obj.response_formation(
                            response['result']['response']['data'], status.HTTP_400_BAD_REQUEST)
                        return Response(response, status=status_code)
                    (
                        response,
                        status_code) = res_obj.response_formation(
                        'Enabling DHCP may end your current management session. In that case, please login using the new IP address and update the new ISE IP in ISE Management.',
                        status.HTTP_504_GATEWAY_TIMEOUT)
                    return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation(
            'Connection Refused', status.HTTP_504_GATEWAY_TIMEOUT)
        return Response(response, status=status_code)

    def network_update(self, ise_id=None, get_url=[], dns_data={}, ip_data={}, ipaddress=None, port_number=None):
        '''This is for update network 1 and 2 data'''
        ip_status = False
        if get_url == status.HTTP_404_NOT_FOUND:
            response = {
                'message': 'fail',
                'status_code': '404',
                'result': 'ISE Not Found'}
        elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
            response = {
                'message': 'fail',
                'status_code': '504',
                'result': 'Connection Refused'}
        else:
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['network']

            if ipaddress:
                ip_status = ip_ping(ipaddress)
            if ip_status:
                response = {
                    'message': 'fail',
                    'status_code': '400',
                    'result': 'IP already exists'}
                return response
            else:
                if dns_data:
                    response = req_obj.send_request(
                        url, AUTH, headers=HEADER_JSON, data=dns_data, method='PUT')
                    if response['result']['status_code'] == 400:
                        response = {
                            'message': 'fail',
                            'status_code': '400',
                            'result': response['result']['response']['data']}
                        return response

                if 'ipaddress' in ip_data or 'ipmask' in ip_data or 'gateway' in ip_data:
                    url = url_dynamic + \
                        RESOURCE['network'] + "/ports/" + str(port_number)
                    response = req_obj.send_request(
                        url, AUTH, headers=HEADER_JSON, data=ip_data, method='PUT')

                if response['message'] == 'success':
                    ise = ListIse.objects.get(id=ise_id)
                    if ipaddress and port_number == 1:
                        ise.ip_primary = ipaddress
                        ise.save()
                    if ipaddress and port_number == 2:
                        ise.ip_secondary = ipaddress
                        ise.save()
                    response = {
                        'message': 'success',
                        'status_code': '200',
                        'result': 'Network Updated Successfully'}
                    return response
                if response['message'] == 'fail' or response['message'] == 'error':
                    response = {
                        'message': 'fail',
                        'status_code': str(
                            response['result']['status_code']),
                        'result': response['result']['response']['data']}
                    return response


class NetworkDetail(APIView):
    '''To get and update particular network details'''

    def __init__(self):
        '''This is for initialize class variables'''
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, ise_id, network_id, format=None):
        '''This is for get particular network 1 or 2 details'''
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
            url = url_dynamic + RESOURCE['network'] + "/ports/" + network_id
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

    def get(self, request, ise_id, network_id, format=None):
        '''This is for get Network details'''
        return self.get_object(ise_id, network_id)

    def put(self, request, ise_id, network_id, format=None):
        '''This is for update particular network based on it's id
            {
                        "led":"disabled"
                }
        '''
        get_url = dynamic_url(ise_id)
        if not isinstance(get_url, int):
            url_dynamic = get_url[0]
            AUTH = get_url[1]
            url = url_dynamic + RESOURCE['network'] + "/ports/" + network_id
            res = req_obj.send_request(
                url,
                AUTH,
                headers=HEADER_JSON,
                data=request.data,
                method='PUT')
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.response_formation(
                'Connection Refused...', status.HTTP_504_GATEWAY_TIMEOUT)
            return Response(response, status=status_code)
