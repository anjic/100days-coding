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


class HostsList(APIView):
    """To get all Hosts"""
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
            url = url_dynamic+RESOURCE['hosts']
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
            self.cortex_total = timeit.default_timer() - self.cortex_start
            (response, status_code) = res_obj.client_response(res, time_res=True)
            if response.get('message') == 'success':
                host_res = response['result']['response']['data']['hosts']

                if host_res.has_key('host'):
                    host_res['host']['ise_id'] = ise_id
                    host_res['host']['host_id'] = host_res['host']['id']
                    if host_res['host']['allocations'].has_key('allocation'):
                        host_res['host']['allocation']= [host_res['host']['allocations']['allocation']]
                    else:
                        host_res['host']['allocation']= host_res['host']['allocations']['allocations']

                elif host_res.has_key('hosts'):
                    for hosts in host_res['hosts']:
                        hosts['host_id'] = hosts['id']
                        hosts['ise_id'] = ise_id
                        if hosts['allocations'].has_key('allocation'):
                            # hosts['allocation'] = []
                            hosts['allocation']=[hosts['allocations']['allocation']]
                        else:
                            hosts['host_id'] = hosts['id']
                            hosts['ise_id'] = ise_id
                            for hosts in host_res['hosts']:
                                # hosts['allocation'] = []
                                if hosts['allocations'].has_key('allocations'):
                                    hosts['allocation']=hosts['allocations']['allocations']
                                else:
                                    hosts['allocation']=[hosts['allocations']['allocation']]
                else:
                    pass

                total_time = timeit.default_timer() - start_time
                process_time = total_time - self.cortex_total
                if response.has_key('time_taken'):
                    response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
                    response['time_taken']['python'] = "%.2fs"%process_time
                    response['time_taken']['total'] = "%.2fs"%total_time
                    response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                    response['time_taken']['req_recv_time'] = "%d"%int(start_time)
                return Response(response, status=status_code)
                
            else:
               return Response(response, status=status_code)

    # @User_Permision('add_host')
    def post(self, request, ise_id, format=None):
        volume_name = request.data['volumes']
        host_name = request.data['name']
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
            url = url_dynamic+RESOURCE['hosts']
            query_string = urllib.urlencode(request.data,doseq=True)
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON, data=query_string, method='POST')
            all_payload = {}
            presentation_res = []

            if res['message'] == 'success':
                allocation_url = url_dynamic+RESOURCE['allocations']
                all_payload['hostname'] = host_name     
                for volumes in volume_name:
                    if volumes['volume'] != False:
                        all_payload['volumename'] = volumes['label']
                        all_payload['lun'] = volumes['lun']
                        allocation_res  = req_obj.send_request(allocation_url, AUTH, headers=HEADER_JSON, data=all_payload, method='POST')
                        presentation_res.append(allocation_res)
            (response, status_code) = res_obj.client_response(res)
            response['result']['response']['secondary_data'] = presentation_res
            return Response(response, status=status_code)

class HostDetail(APIView):
    """Retrieve,Update or Delete a hosts instance"""
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    def get_object(self, ise_id, hostid):
        """To get particular object"""
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
            url = url_dynamic+RESOURCE['hosts']+"/"+hostid
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON)
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

    def get(self, request, ise_id, hostid, format=None):
        """Get particular volume based on it's id"""
        return self.get_object(ise_id,hostid)

    # @User_Permision('change_host')
    def put(self, request, ise_id, hostid, format=None):
        """Update particular volume based on it's id
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
            url = url_dynamic+RESOURCE['hosts']+"/"+hostid
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

    # @User_Permision('delete_host')
    def delete(self, request, ise_id, hostid, format=None):
        """Delete particular volume based on it's id"""
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
            url = url_dynamic+RESOURCE['hosts']+"/"+hostid
            res  = req_obj.send_request(url, AUTH, headers=HEADER_JSON, method='DELETE')
            if res['message'] == 'success':
                (response, status_code) = res_obj.response_formation({'deleted_host':hostid},status.HTTP_200_OK)
                return Response(response, status=status_code)
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)

class Allocation(APIView):
    """mapping host with multiple volumes """
    def put(self, request, ise_id,hostid, format=None):
        
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
            req = dict(request.data)
            re_present = []
            res = {
                'allocation' : [],
                'unallocation' : [],
                'changed' : [],
                }

            if req.get('unpresent'):
                for allocationid in req['unpresent']:
                    upr_url = allocation_url = url_dynamic + RESOURCE['allocations'] + "/" + str(allocationid)
                    upr_res = req_obj.send_request(upr_url, AUTH, headers=HEADER_JSON, method='DELETE')
                    res['unallocation'].append(upr_res.get('result'))

            if req.get('present'):
                pr_url = allocation_url = url_dynamic + RESOURCE['allocations']
                temp = {}
                temp['hostname'] = req['host_name']
                for volume_name in req['present']:
                    temp['volumename'] = volume_name['name']
                    temp['lun'] = volume_name['lun']
                    data_string = urllib.urlencode(temp)
                    pr_res = req_obj.send_request(pr_url, AUTH, headers=HEADER_JSON, data=data_string, method='POST')

                    if pr_res.get('message') == 'fail':
                        re_present.append('Status code :'+str(pr_res['result']['status_code']) +' - '+ volume_name.get('name'))
                    res['allocation'].append(pr_res.get('result'))

            if req.get('changed'):
                temp = {}
                for allocationid in req['changed']:
                    temp['lun'] = allocationid['lun']
                    data_string = urllib.urlencode(temp)
                    modify_url = url_dynamic + RESOURCE['allocations'] + "/" + str(allocationid['global_id'])
                    change_res = req_obj.send_request(modify_url, AUTH, headers=HEADER_JSON, data=data_string, method='PUT')
                    if change_res.get('message') == 'fail':
                        re_present.append('Status code :'+str(change_res['result']['status_code'])+' - '+str(allocationid.get('lun'))+' - '+change_res['result']['response']['data']+' ')
                    res['changed'].append(change_res.get('result'))

            if re_present:
                (response, status_code) = res_obj.response_formation({'success':res,'retry_lun':re_present}, status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)

            (response, status_code) = res_obj.response_formation(res, status.HTTP_200_OK)
            return Response(response, status=status_code)