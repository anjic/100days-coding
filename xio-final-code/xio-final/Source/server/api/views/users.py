from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
import timeit

from django.contrib.auth.models import User
from api.models.ise_models import ListIse
from api.serializer.user_serializer import UserSerializer
from lib.client_response import ClientResponse
from config import (secret)
from config import secret

res_obj = ClientResponse()


class UsersList(APIView):
    """List of Users and Create New Users"""

    def get(self, request, format=None):
        """This is for getting a list of users"""
        start_time = timeit.default_timer()
        users = User.objects.all()
        user = UserSerializer(users, many=True)

        for i in range(len(user.data)):
            user.data[i].setdefault('sudo_user', False)
            if user.data[i].get('username') == 'Administrator':
                user.data[i]['sudo_user'] = True
        (response, status_code) = res_obj.response_formation(
            user.data, status.HTTP_200_OK, time_res=True)
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
        """This is for creating a new user"""
        user_info = request.data
        try:
            user = User.objects.create_user(
                user_info['username'],
                user_info['email'],
                user_info['password'])
            user.first_name = user_info['first_name']
            user.last_name = user_info['last_name']
            user.save()
            (response, status_code) = res_obj.response_formation(
                'New User Created Succesfully', status.HTTP_201_CREATED)
            return Response(response, status=status_code)

        except Exception as e:
            (response, status_code) = res_obj.response_formation(
                str(e), status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)


class UserDetails(APIView):
    """Get user information and delete the user based on user id"""

    def get_object(self, id):
        """This is for getting particular User object"""
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        """Get particular User based on it's id"""
        start_time = timeit.default_timer()
        user_obj = self.get_object(id)
        if user_obj:
            user_serializer = UserSerializer(user_obj)
            (response, status_code) = res_obj.response_formation(
                user_serializer.data, status.HTTP_200_OK, time_res=True)
            total_time = timeit.default_timer() - start_time
            if 'time_taken' in response:
                response['time_taken']['req_recv_time'] = "%d" % int(
                    start_time)
                response['time_taken']['cortex'] = "0.0s"

                response['time_taken']['python'] = "%.2fs" % total_time
                response['time_taken']['total'] = "%.2fs" % total_time
                response['time_taken']['res_send_time'] = "%d" % int(
                    timeit.default_timer())
            return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation(
            'User Not Found', status.HTTP_404_NOT_FOUND, time_res=True)
        total_time = timeit.default_timer() - start_time
        if 'time_taken' in response:
            response['time_taken']['cortex'] = "0.0s"
            response['time_taken']['python'] = "%.2fs" % total_time
            response['time_taken']['total'] = "%.2fs" % total_time
            response['time_taken']['res_send_time'] = "%d" % int(
                timeit.default_timer())
        return Response(response, status=status_code)

    def put(self, request, id, format=None):
        """This is for updating particular User based on it's id"""
        user_info = request.data
        token = request.META['HTTP_AUTHORIZATION']
        session_user = jwt.decode(token[4:], secret, algorithm='HS256')
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            (response, status_code) = res_obj.response_formation(
                serializer.data, status.HTTP_200_OK)
            return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.response_formation(
                serializer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status_code)

    def delete(self, request, id, format=None):
        """This is for deleting particular User based on it's id"""
        token = request.META['HTTP_AUTHORIZATION']
        session_user = jwt.decode(token[4:], secret, algorithm='HS256')
        user_obj = User.objects.get(id=id)

        if user_obj.username == session_user['username']:
            (response, status_code) = res_obj.response_formation(
                'User cannot delete own account', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)
        else:
            user_obj.delete()
            (response, status_code) = res_obj.response_formation(
                {'deleted_user': user_obj.username}, status.HTTP_200_OK)
            return Response(response, status=status_code)


class Login(APIView):
    """User login to access all managements"""

    def get_object(self, name):
        """This is for getting particular User object"""
        try:
            return User.objects.get(username=name)
        except User.DoesNotExist:
            return False

    def post(self, request, format=None):
        """This is for checking given username and password are correct"""
        user = self.get_object(request.data['username'])
        if user:
            if user.check_password(request.data['password']):
                if user.is_active:
                    token = jwt.encode(
                        {'username': request.data['username']}, secret, algorithm='HS256')
                    try:
                        ise = ListIse.objects.get(prefered=1)
                        (response, status_code) = res_obj.response_formation(
                            {'token': token, 'username': request.data['username']}, status.HTTP_200_OK)
                        response['result']['response']['data']['user_privilege'] = {
                            'prefered_ise': ise.id}
                        return Response(response, status_code)
                    except BaseException:
                        (response, status_code) = res_obj.response_formation(
                            {'token': token, 'username': request.data['username']}, status.HTTP_200_OK)
                    return Response(response, status=status_code)
                else:
                    (response, status_code) = res_obj.response_formation(
                        'User is not active', status.HTTP_400_BAD_REQUEST)
                    return Response(response, status=status_code)
            else:
                (response, status_code) = res_obj.response_formation(
                    'Invalid Username or Password', status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)

        (response, status_code) = res_obj.response_formation(
            'Invalid Username or Password', status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status_code)


class UserPassword(APIView):
    """Update user password"""

    def get_object(self, user_name):
        """To get particular User object"""
        try:
            return User.objects.get(username=user_name)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        """Update particular UserPassword based on it's id"""
        try:
            token = request.META['HTTP_AUTHORIZATION']
            session_user = jwt.decode(token[4:], secret, algorithm='HS256')
            user = self.get_object(session_user['username'])
        except BaseException:
            (response, status_code) = res_obj.response_formation(
                'Token Not Provided', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)

        if user.username == session_user['username']:
            current = request.data['curr_password']
            new = request.data['new_password']
            confirm = request.data['confirm_password']

            if user.check_password(current):
                if user.check_password(new):
                    (response, status_code) = res_obj.response_formation(
                        'Password cannot be same', status.HTTP_400_BAD_REQUEST)
                    return Response(response, status=status_code)
                else:
                    if new == confirm:
                        user.set_password(new)
                        user.save()
                        (response, status_code) = res_obj.response_formation(
                            'Password Changed Succesfully', status.HTTP_201_CREATED)
                        return Response(response, status=status_code)
                    else:
                        (response, status_code) = res_obj.response_formation(
                            'Password doesnot match', status.HTTP_400_BAD_REQUEST)
                        return Response(response, status=status_code)
            else:
                (response, status_code) = res_obj.response_formation(
                    'Invalid Password', status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.response_formation(
                'Invalid User', status.HTTP_400_BAD_REQUEST)
            return Response(response, status=status_code)