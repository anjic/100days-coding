import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(BASE_DIR, 'conf/')
LOG_DIR = os.path.join(BASE_DIR, 'logs/')
KEYS_DIR = os.path.join(BASE_DIR, 'keys')
XIO_DIR = os.path.join(BASE_DIR, 'xio_ise')
XML_DIR = os.path.join(BASE_DIR, 'xmltojson/')
ssl_certificate = '/etc/ssl/certs/ssl-cert-snakeoil.pem'
ssl_certificate_key = '/etc/ssl/private/ssl-cert-snakeoil.key'

# Default log setting is False
log_required = False
