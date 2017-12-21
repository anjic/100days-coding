from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from xio_ise.local_settings import CONF_DIR, BASE_DIR
import ConfigParser
import os
import timeit

# custome imports
from api.models.ise_models import ListIse
from api.models.settings import MailUser,SMTPConfig
from api.serializer.settings_serializers import MailUserSerializer
from utility.encryption import encryption, decryption
from lib.client_response import ClientResponse
res_obj = ClientResponse()

# creating config object
config = ConfigParser.RawConfigParser()
config.add_section('delay')
config.add_section('smtp')


class MailUserList(APIView):
    '''List of Users and Create New Users'''
    def get(self, request, ise_id, format=None):
        start_time = timeit.default_timer()
        users = MailUser.objects.filter(ise_id=ise_id)
        user = MailUserSerializer(users, many=True)
        (response, status_code) = res_obj.response_formation(user.data,
                                                             status.HTTP_200_OK, time_res=True)

        total_time = timeit.default_timer() - start_time
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)

    # @User_Permision('add_mailuser')
    def post(self, request, ise_id, format=None):

        # ise_id = ListIse.objects.get(id=ise_id)
        request.data['ise_id'] = ise_id
        serializer = MailUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            (response, status_code) = res_obj.response_formation('New User Created Succesfully',
                status.HTTP_201_CREATED)
            return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.response_formation('Missing Parameter or Bad Request',
                                                                    status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)


class MailUserDetails(APIView):
    '''Get user information and delete the user based on user id'''

    def get_object(self, ise_id, user_id):
        """To get particular User object"""
        try:
            return MailUser.objects.get(id=user_id, ise_id=ise_id)
        except MailUser.DoesNotExist:
            raise Http404

    def get(self, request, ise_id, user_id, format=None):
        """Get particular User based on it's user_id"""
        start_time = timeit.default_timer()
        user_obj = self.get_object(ise_id, user_id)
        user_serializer = MailUserSerializer(user_obj)
        (response, status_code) = res_obj.response_formation(user_serializer.data,
                                                                    status.HTTP_200_OK, time_res=True)

        total_time = timeit.default_timer() - start_time
        if response.has_key('time_taken'):
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs"%total_time
            response['time_taken']['total'] = "%.2fs"%total_time
            response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
            response['time_taken']['req_recv_time'] = "%d"%int(start_time)
        return Response(response, status=status_code)

    # @User_Permision('change_mailuser')
    def put(self, request, ise_id, user_id, format=None):
        """Update particular User based on it's user_id"""

        user = self.get_object(user_id=user_id,ise_id=ise_id)
        serializer = MailUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            (response, status_code) = res_obj.response_formation('MailUser Updated Succesfully',status.HTTP_200_OK)
            return Response(response, status=status_code)
        (response, status_code) = res_obj.response_formation('Missing Parameter or Bad Request',status.HTTP_400_BAD_REQUEST)
        return Response(response, status_code)

    # @User_Permision('delete_mailuser')
    def delete(self, request, ise_id, user_id, format=None):
        """Delete particular User based on it's user_id"""
        
        user_obj = self.get_object(ise_id, user_id)
        user_obj.delete()
        (response, status_code) = res_obj.response_formation({"deleted_mailuser":user_obj.name},
                                                                    status.HTTP_200_OK)
        return Response(response, status=status_code)

class Schedule(APIView):

    def get(self, request, format=None):
        return Response('test')

    def post(self, request, format=None):

        data = request.data
        config.set('delay', 'aggregator', data.get('aggregator',20))
        config.set('delay', 'collector', data.get('collector',20))
        config.set('delay', 'logs', data.get('logs',20))
        config.set('delay', 'publisher', data.get('publisher',20))
        config.set('delay', 'alert_mail', data.get('alert_mail',20))
        if os.path.exists(BASE_DIR + '/conf'):
            with open(CONF_DIR + 'schedule.cfg', 'wb') as configfile:
                config.write(configfile)
        else:
            os.makedirs(BASE_DIR + '/conf')
            with open(CONF_DIR + 'schedule.cfg', 'wb') as configfile:
                config.write(configfile)
        (response, status_code) = res_obj.response_formation('data updated successfully',
                                                             status.HTTP_201_CREATED)
        return Response(response, status=status_code)

class Smtp(APIView):
    def get(self, request, format=None):
        start_time = timeit.default_timer()
        try:
            smtp = SMTPConfig.objects.first()
            smtp_info = {}
            smtp_info['email_host'] = smtp.email_host
            smtp_info['email_host_user'] = smtp.email_host_user
            smtp_info['email_host_password'] = smtp.email_host_password
            smtp_info['email_port'] = smtp.email_port
            smtp_info['enable_authentication'] = smtp.enable_authentication
            smtp_info['use_ssl_tl'] = smtp.use_ssl_tl
            smtp_info['from_mail'] = smtp.from_mail
            (response, status_code) = res_obj.response_formation(smtp_info,
                                                             status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            if response.has_key('time_taken'):
                response['time_taken']['cortex'] = "0.0s"
                response['time_taken']['python'] = "%.2fs"%total_time
                response['time_taken']['total'] = "%.2fs"%total_time
                response['time_taken']['res_send_time'] = "%d"%int(timeit.default_timer())
                response['time_taken']['req_recv_time'] = "%d"%int(start_time)
            return Response(response, status_code)
        except Exception as e:
            (response, status_code) = res_obj.response_formation({},status.HTTP_200_OK)
            return Response(response, status_code)


    def post(self, request, format=None):

        data = request.data

        smtp = SMTPConfig.objects.first()
        
        if not smtp:
            smtp = SMTPConfig()
        
        smtp.email_host = data.get('email_host')
        smtp.email_host_user = data.get('email_host_user')
        if data.has_key('email_host_password'):
            if data['email_host_password']:
                smtp.email_host_password = encryption(data.get('email_host_password'))
            else:
                smtp.email_host_password = data.get('email_host_password')
            
        smtp.email_port = data.get('email_port')
        smtp.enable_authentication = data.get('enable_authentication',False)
        smtp.use_ssl_tl = data.get('use_ssl_tl',False)
        smtp.from_mail = data.get('from_mail')
        smtp.save()

        (response, status_code) = res_obj.response_formation('data updated successfully',
                                                             status.HTTP_201_CREATED)
        return Response(response, status=status_code)
