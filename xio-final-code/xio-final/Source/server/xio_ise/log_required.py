from xio_ise.local_settings import log_required


def is_log_required(info=True, message='', log=log_required, logger_info=None):
    '''
        This is for monitoring all services using log record.
        If info is True,logs the record as information else it logs as error.
        '''
    if log:
        if info:
            logger_info.info(message)
        else:
            logger_info.error(message)
