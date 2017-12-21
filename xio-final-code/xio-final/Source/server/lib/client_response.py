# other library
from xio_ise.settings import DEBUG


class ClientResponse():
    '''This is for formatting the response'''

    def client_response(self, res, time_res=False, successfull_ip=None):
        '''This is for formatting the response and returns it'''
        response_data = {}

        if DEBUG and time_res:
            response_data['time_taken'] = {
                "cortex": "",
                "total": "",
                "python": "",
                "req_recv_time": "",
                "res_send_time": ""
            }

        response_data['message'] = "success"

        result_json = res.get('result', None)

        if res["message"] == "success":
            response_data['result'] = {}
            response_data['result']['status_code'] = result_json['status_code']
            response_data['result']['response'] = {}
            response_data['result']['response']['data'] = result_json['response']['data']
            response_data['result']['error'] = False

            if successfull_ip:
                response_data['ip'] = successfull_ip

            return (response_data, result_json['status_code'])

        elif res["message"] == "fail":
            error_data = result_json['response']['data']
            result_json['response']['data'] = []
            response_data['result'] = {}
            response_data['result']['response'] = {}
            response_data['result']['response']['data'] = result_json['response']['data']
            response_data['result']['status_code'] = result_json['status_code']
            response_data['result']['error'] = {
                "status_code": result_json['status_code'],
                "message": error_data}
            response_data["message"] = "fail"
            return (response_data, result_json['status_code'])

        else:
            error_data = result_json['response']['data']
            result_json['response']['data'] = []
            response_data['result'] = {}
            response_data['result']['response'] = {}
            response_data['result']['response']['data'] = result_json['response']['data']
            response_data['result']['status_code'] = result_json['status_code']
            response_data['result']['error'] = {
                "status_code": result_json['status_code'],
                "message": error_data}
            response_data["message"] = "fail"
            return (response_data, result_json['status_code'])

    def response_formation(self, response, status_code, time_res=False):
        '''This is for formatting the response and returns it'''

        response_data = {}

        if DEBUG and time_res:
            response_data['time_taken'] = {
                "cortex": "",
                "total": "",
                "python": "",
                "req_recv_time": "",
                "res_send_time": ""
            }

        if str(status_code)[0] == '2':
            response_data['message'] = "success"
            response_data['result'] = {'response': {"data": response},
                                       'status_code': status_code,
                                       'error': False}

        else:
            response_data['message'] = "fail"
            response_data['result'] = {'response': {"data": []},
                                       'status_code': status_code,
                                       'error': {"status_code": status_code,
                                                 "message": response}}
        return (response_data, status_code)