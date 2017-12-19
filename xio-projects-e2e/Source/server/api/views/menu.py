from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import gevent
import timeit

from api.models.sangroup_models import SanGroup, SanIse
from api.models.ise_models import (ListIse, SangroupIse)
from api.models.servermgmt_models import SangroupServer,ServerMgmt
from utility.dynamic_url_formation import dynamic_url

from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE)
from utility.global_log import local_logger

req_obj = GenericRequests()
res_obj = ClientResponse()

class Sidemenu(APIView):
    ''' To get dynamic information about side panel
    '''
    def __init__(self):
        self.cortex_start = 0.0
        self.cortex_total = 0.0

    # def collect_data(self,request_details={}):

    #     result = []
    #     res = req_obj.send_request(request_details.get('url'), request_details.get('auth'), headers=HEADER_JSON)
    #     if res['message'] == 'success':
    #         host_data = res['result']['response']['data']['hosts']
    #         host_list = []

    #         if 'hosts' in host_data:
    #             host_list.extend(host_data['hosts'])

    #         elif 'host' in host_data:
    #             host_list.append(host_data['host'])
                
    #         for host in host_list:
    #             result.append({'ise_id':request_details.get('ise_id'), 'hosts': host['name'], 'host_id': host['id']})

    #     return result



    def get(self, request, format=None):

        start_time = timeit.default_timer()
        end_result = None
        sangroups = SanGroup.objects.values('sangroup_name', 'sangroup_id')

        for sg_id in sangroups:
            san_ise = SangroupIse.objects.values('ise_id').filter(sg_id=sg_id['sangroup_id'])
            san_server = SangroupServer.objects.values('server_id_id').filter(san_id=sg_id['sangroup_id'])
            list_ise = ListIse.objects.values('ise_name', 'id').filter(id__in=san_ise)
            list_server = ServerMgmt.objects.values('server_name', 'server_id').filter(server_id__in=san_server)
            sg_id['ise'] = [data for data in list_ise]
            sg_id['server'] = [data for data in list_server]
            sg_id['hosts'] = []
            threads = []

            for i, ise in enumerate(list_ise):
                get_url = dynamic_url(ise['id'])

                if get_url == status.HTTP_404_NOT_FOUND:
                    continue
                   
                elif get_url == status.HTTP_504_GATEWAY_TIMEOUT:
                    continue
                    
                else:
                    urls_details = {
                        'url': get_url[0]+RESOURCE['hosts'],
                        'auth': get_url[1],
                        'ise_id': ise['id']
                    }
                    self.cortex_start = timeit.default_timer()
                    # threads.append(gevent.spawn(self.collect_data, request_details=urls_details))
            # end_result = gevent.joinall(threads)
            # self.cortex_total = self.cortex_total+(timeit.default_timer() - self.cortex_start)
            # # print "$$$$",[thread.value for thread in threads]

            # for thread in threads:
            #     sg_id['hosts'].extend(thread.value)

        (response, status_code) = res_obj.response_formation(sangroups, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        process_time = total_time - self.cortex_total
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "%.2fs"%self.cortex_total
            response['time_taken']['python'] = "%.2fs"%process_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        # local_logger.info('%s,%.2fs,%s'%(request.get_full_path(),timeit.default_timer() - start_time,request.resolver_match.view_name))
        # local_logger.info('%s,%.2fs,%.2fs,%.2fs'%(request.get_full_path(), total_time, self.cortex_total, process_time))
        return Response(response, status_code)
