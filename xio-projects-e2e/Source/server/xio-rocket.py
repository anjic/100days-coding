#!/usr/bin/env python
from rocket import Rocket
from xio_ise.wsgi import application as xio_wsgi

server = Rocket(
    ('127.0.0.1', 8000), 'wsgi', {
        "wsgi_app": xio_wsgi}, min_threads=64, max_threads=64)
server.start()
