from django.conf import settings
import timeit

from utility.global_log import local_logger


class LoggingMiddleware(object):

    def process_request(self, request):
        if settings.DEBUG:
            request._request_time = timeit.default_timer()
            # request._start_time = timeit.default_timer()
            # print "$$$$$$",request.get_full_path()
            # print request,dir(request)

        return None

    def process_response(self, request, response):
        if settings.DEBUG:
            # response_time = request._request_time - datetime.now()
            # print "time in seconds",timeit.default_timer() - request._request_time
            local_logger.info('%s,%.2fs'%(request.get_full_path()
                ,timeit.default_timer() - request._request_time))

            # print "$$$$$$",dir(response),response.data
        return response