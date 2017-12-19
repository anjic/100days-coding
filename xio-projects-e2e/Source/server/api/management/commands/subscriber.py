from django.core.management.base import BaseCommand
import gevent
import zmq.green as zmq
from geventwebsocket.handler import WebSocketHandler
import logging

#creating logger object
from xio_ise.local_settings  import (LOG_DIR,KEYS_DIR,
                                    ssl_certificate,ssl_certificate_key)
from xio_ise.log_required import is_log_required
from config import (SOCKET_IP, SOCKET_PORT, WS_PORT, WSS)

logger = logging.getLogger('subscriber')
hdlr = logging.FileHandler(LOG_DIR + 'subscriber.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)



class WebSocketApp(object):
    """
    """

    def __init__(self, context):
        self.context = context

    def __call__(self, environ, start_response):
        ws = environ['wsgi.websocket']
        sock = self.context.socket(zmq.SUB)
        sock.setsockopt(zmq.SUBSCRIBE, "")
        sock.connect('inproc://queue')
        while True:
            data = sock.recv()
            ws.send(data)

class Command(BaseCommand,WebSocketApp):

    def handle(self, *args, **options):

        try:
            context = zmq.Context()
            gevent.spawn(self.zmq_server, context)

            if WSS:
                ws_server = gevent.pywsgi.WSGIServer(
                    ('', WS_PORT), WebSocketApp(context),
                    handler_class=WebSocketHandler,
                    certfile=ssl_certificate,
                    keyfile=ssl_certificate_key)
            else:
                ws_server = gevent.pywsgi.WSGIServer(
                    ('', WS_PORT), WebSocketApp(context),
                    handler_class=WebSocketHandler)
                
            ws_server.start()
            ws_server.serve_forever()
            
        except Exception as e:
            #logger.error(e)
            is_log_required(info=True, message=e,  logger_info=logger)

    def zmq_server(self, context):

        sock_incoming = context.socket(zmq.SUB)
        sock_outgoing = context.socket(zmq.PUB)
        sock_incoming.bind('tcp://*:%s'%SOCKET_PORT)
        sock_outgoing.bind('inproc://queue')
        sock_incoming.setsockopt(zmq.SUBSCRIBE, "")

        while True:
            data = sock_incoming.recv()
            #logger.info(data)
            is_log_required(info=True, message = data,  logger_info=logger)
            sock_outgoing.send(data)
            #logger.info("subscriber receiving data")
            is_log_required(info=True, message = 'subscriber receiving data',  logger_info=logger)


