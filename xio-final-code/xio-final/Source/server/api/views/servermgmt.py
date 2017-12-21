from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import timeit
from django.db.models import Q

from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from api.models.sangroup_models import SanGroup
from api.models.servermgmt_models import ServerMgmt,SangroupServer
from api.serializer.servermgmt_serializer import ServerMgmtSerializer
from utility.dynamic_url_formation import dynamic_url
from config import (AUTH, HEADER_JSON, RESOURCE)

req_obj = GenericRequests()
res_obj = ClientResponse()


class ServerMgmtList(APIView):
    """List all ServerMgmt, or create ServerMgmt """

    def get(self, request, format=None):
    	start_time = timeit.default_timer()
    	servermgmt = ServerMgmt.objects.all()
    	serializer = ServerMgmtSerializer(servermgmt, many=True)

        for server_id in serializer.data:
            san_server = SangroupServer.objects.values('san_id').filter(server_id=server_id['server_id'])
            list_san = SanGroup.objects.values('sangroup_id', 'sangroup_name').filter(sangroup_id__in=san_server)
            server_id['sangroup'] = [data for data in list_san]

    	(response, status_code) = res_obj.response_formation(serializer.data,status.HTTP_200_OK, time_res=True)
    	total_time = timeit.default_timer() - start_time

    	if response.has_key('time_taken'):
    		response['time_taken']['cortex'] = "0.0s"
    		response['time_taken']['python'] = "%.2fs"%total_time
    		response['time_taken']['total'] = "%.2fs"%total_time
    		response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
    		response['time_taken']['req_recv_time'] = "%d"%int(start_time)
    	return Response(response, status=status_code)

    def post(self, request, format=None):
        """create server list"""
        san_server = request.data.get('sangroup')
        del request.data['sangroup']
        serializer = ServerMgmtSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            server = ServerMgmt.objects.get(server_name = request.data['server_name'])

            if san_server:
                for san_id in san_server:
                    san = SangroupServer()
                    san.server_id_id = ServerMgmt.objects.get(server_name = request.data['server_name']).server_id
                    san.san_id = SanGroup.objects.get(sangroup_id = san_id)
                    san.save()
            (response, status_code) = res_obj.response_formation(serializer.data,status.HTTP_201_CREATED)
            return Response(response, status=status_code)

        if serializer.errors['server_name']:
            (response, status_code) = res_obj.response_formation("ServerName already exists",status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status_code)


class ServerMgmtDetail(APIView):
    """
    """
    def delete(self, request, id, format=None):
        """Delete particular server based on it's id if not present in any ise"""

        san = SangroupServer.objects.filter(server_id=id)
        if san:
            (response, status_code) = res_obj.response_formation('Server Mapped with one or more sangroup',
                                                                 status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)

        server_mgmt = ServerMgmt.objects.get(server_id=id)
        server_mgmt.delete()
        (response, status_code) = res_obj.response_formation({'deleted_server':server_mgmt.server_name},
                                                         status.HTTP_200_OK)
        return Response(response, status=status_code)

class SanServerMap(APIView):
    '''get all sangroup list for selected ise'''

    def get(self, request, id, format=None):
        start_time = timeit.default_timer()
        san_list = SanGroup.objects.values('sangroup_id', 'sangroup_name')

        for san in san_list:
            server = SangroupServer.objects.all().filter(Q(san_id=san['sangroup_id']) & Q(server_id=id))
            if server:
                san['checked'] = True
            else:
                san['checked'] = False

        (response, status_code) = res_obj.response_formation(san_list, status.HTTP_200_OK, time_res=True)
        total_time = timeit.default_timer() - start_time
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)

    def put(self, request, id, format=None):
        ''' mapping sangroup with selected ise  '''
        for server_id in request.data['added']:
            san = SangroupServer()
            san.san_id = SanGroup.objects.get(sangroup_id=server_id)
            san.server_id = ServerMgmt.objects.get(server_id=id)
            san.save()

        for san_id in request.data['removed']:
            san = SangroupServer.objects.filter(Q(san_id=san_id) & Q(server_id=id)).delete()
        (response, status_code) = res_obj.response_formation('Mapping Done Successfully',
                                                             status.HTTP_200_OK)
        return Response(response, status=status_code)

