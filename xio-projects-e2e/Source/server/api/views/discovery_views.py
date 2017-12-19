from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# other library
from lib.generic_request import GenericRequests
from lib.client_response import ClientResponse
from config import (AUTH, HEADER_JSON, RESOURCE)

req_obj = GenericRequests()
res_obj = ClientResponse()


class Discovery(APIView):
    """
        Get Discovery details

        request json = {
            "primary_ip":"10.20.225.136",
            "secondary_ip":"10.20.225.136",
            "user_name":"muthu",
            "user_password":"xxxx"
        }
    """
    def post(self, request, format=None):

        req_data = request.data
        primary_url = "http://" + str(req_data['primary_ip']) + "/query"
        res = req_obj.send_request(primary_url, (req_data['user_name'], req_data['user_password']), headers=HEADER_JSON)
        if res['message'] == 'success':
            get_url = res['result']['response']['data']['array']['_attr']['self']
            get_res = req_obj.send_request(get_url, (req_data['user_name'], req_data['user_password']), headers=HEADER_JSON)

            if get_res['message'] == 'success':
                array_details = get_res['result']['response']['data']['arrays']['array']
                res['result']['response']['data']['array']['contactphone'] = array_details['contactphone']
                res['result']['response']['data']['array']['contactemail'] = array_details['contactemail']
                res['result']['response']['data']['array']['contactname'] = array_details['contactname']
                res['result']['response']['data']['array']['location'] = array_details['location']
                res['result']['response']['data']['array']['address'] = array_details['address']
                (response, status_code) = res_obj.client_response(res)
                return Response(response, status=status_code)
            elif get_res['result']['status_code'] == 401:
                (response, status_code) = res_obj.response_formation('Invalid Username or Password', status.HTTP_401_UNAUTHORIZED)
                return Response(response, status=status_code)
            else:
                (response, status_code) = res_obj.response_formation(get_res, status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status_code)
        else:
            (response, status_code) = res_obj.client_response(res)
            return Response(response, status=status_code)
