import logging
from xio_ise.local_settings import LOG_DIR


local_logger = logging.getLogger('request_log')
shdlr = logging.FileHandler(LOG_DIR + 'request_local_time.csv')
sformatter = logging.Formatter('%(message)s')
shdlr.setFormatter(sformatter)
local_logger.addHandler(shdlr)
local_logger.setLevel(logging.INFO)
