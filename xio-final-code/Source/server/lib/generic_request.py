import xml.etree.ElementTree as ET
from json import loads
import os
import logging
import timeit
import requests

# other library
from xio_ise.local_settings import LOG_DIR
from xio_ise.log_required import is_log_required
from utility.xml_to_json_parser import xml_to_json

requests.packages.urllib3.disable_warnings()
logger = logging.getLogger('request')
slogger = logging.getLogger('speed')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

hdlr = logging.FileHandler(LOG_DIR + 'request_detail.log')
shdlr = logging.FileHandler(LOG_DIR + 'request_time.csv')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
sformatter = logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
shdlr.setFormatter(sformatter)
logger.addHandler(hdlr)
slogger.addHandler(shdlr)
logger.setLevel(logging.INFO)
slogger.setLevel(logging.INFO)


class GenericRequests():
    '''This is for common request for given url and return response as JSON'''
    error_code = 504

    request_time = None
    parse_time = None
    total_time = None

    def send_request(self, url, auth, data=None,
                     headers={"Content-Type": "application/xml"},
                     method='GET', to_convert=True, celxml=False):
        '''This is for making common request for given url and returns response as JSON'''
        res_result = {}
        res_result['response'] = {}

        try:
            CODE = 200
            SEND = None
            if method == 'POST':
                CODE = 201
                is_log_required(info=True, message='payload: %s ' % data,
                                logger_info=logger)
                is_log_required(info=True, message='url: %s ' % url,
                                logger_info=logger)
                res = requests.post(url, auth=auth, headers=headers,
                                    data=data, timeout=10, verify=False)
                root = ET.fromstring(res.text.replace("'", '"'))
                SEND = root.text

            elif method == 'PUT':
                CODE = 201
                is_log_required(info=True, message='payload: %s ' % data,
                                logger_info=logger)
                is_log_required(info=True, message='url: %s ' % url,
                                logger_info=logger)
                res = requests.put(url, auth=auth, headers=headers,
                                   params=data, timeout=20, verify=False)
                if res.text:
                    root = ET.fromstring(res.text.replace("'", '"'))
                    SEND = root.text
                else:
                    SEND = "updated successfully"

            elif method == 'DELETE':
                CODE = 204
                is_log_required(info=True, message='payload: %s ' % data,
                                logger_info=logger)
                is_log_required(info=True, message='url: %s ' % url,
                                logger_info=logger)
                res = requests.delete(url, auth=auth, headers=headers,
                                      params=data, verify=False)
                SEND = "success"

            else:
                sts_time = timeit.default_timer()
                is_log_required(info=True, message='payload: %s ' % data,
                                logger_info=logger)
                is_log_required(info=True, message='url: %s ' % url,
                                logger_info=logger)
                start_time = timeit.default_timer()
                res = requests.get(url, auth=auth, headers=headers,
                                   timeout=20, verify=False)
                self.request_time = timeit.default_timer() - start_time
                if to_convert:
                    start_time = timeit.default_timer()
                    SEND = loads(xml_to_json(res.text.encode('ascii','ignore')),
                    		strict=False)
                    self.parse_time = timeit.default_timer() - start_time
                    self.total_time = timeit.default_timer() - sts_time
                elif celxml:
                    start_time = timeit.default_timer()
                    SEND = res.text.encode('ascii', 'ignore')
                    self.parse_time = timeit.default_timer() - start_time
                    self.total_time = self.parse_time
                    return SEND
                else:
                    start_time = timeit.default_timer()
                    SEND = res.text
                    self.parse_time = timeit.default_timer() - start_time
                    self.total_time = self.parse_time

                is_log_required(
                    info=True, message='%s,%s,%.2fs,%.2fs,%.2fs' 
                    	%(method, url, float(
                        self.request_time), float(
                        self.parse_time), float(
                        self.total_time)), logger_info=slogger)

            if res.status_code == 401:
                res_result['response']['data'] = '401 Unauthorized'
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "fail", "result": res_result}

            elif res.status_code == 400:
                res_result['response']['data'] = ET.fromstring(
                    res.text.replace("'", '"')).text
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "fail", "result": res_result}

            elif res.status_code == 404:
                res_result['response']['data'] = ET.fromstring(
                    res.text.replace("'", '"')).text
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "fail", "result": res_result}

            elif res.status_code == 409:
                res_result['response']['data'] = ET.fromstring(
                    res.text.replace("'", '"')).text
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "fail", "result": res_result}

            elif res.status_code == CODE:
                res_result['response']['data'] = SEND
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "success", "result": res_result}

            elif res.text:
                root = ET.fromstring(res.text.replace("'", '"'))
                res_result['response']['data'] = root.text
                res_result['response']['values'] = root.attrib
                res_result['status_code'] = res.status_code
                return {"message": "success", "result": res_result}

            else:
                res_result['response']['data'] = ' '
                res_result['response']['values'] = res.status_code
                res_result['status_code'] = res.status_code
                return {"message": "success", "result": res_result}

        except requests.exceptions.Timeout:
            res_result['response']['data'] = "Request Timeout, Retry.."
            res_result['status_code'] = self.error_code
            return {"message": "error", "result": res_result}

        except requests.exceptions.ConnectionError:
            res_result['response']['data'] = "ConnectionError, Retry.."
            res_result['status_code'] = self.error_code
            return {"message": "error", "result": res_result}

        except requests.exceptions.TooManyRedirects:
            res_result['response']['data'] = "TooManyRedirects.."
            res_result['status_code'] = self.error_code
            return {"message": "error", "result": res_result}

        except requests.exceptions.RequestException:
            res_result['response']['data'] = "RequestException.."
            res_result['status_code'] = self.error_code
            return {"message": "error", "result": res_result}