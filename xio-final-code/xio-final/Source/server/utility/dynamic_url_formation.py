from rest_framework import status

# other library
from api.models.ise_models import ListIse
from lib.generic_request import GenericRequests
from utility.encryption import encryption, decryption
req_obj = GenericRequests()


def dynamic_url(ise_id, https=True, query=False):
    '''
    Returns URL for requested ise_id.
    If https is True, returns URL in https format else it will return in http format.
    If query is True, returns URL for ise query details.
    '''
    IP = None
    ise_details = {}

    try:
        ise_details = ListIse.objects.values('id', 'ip_primary', 'mrc1_status',
                                             'mrc2_status', 'ip_secondary',
                                             'serial_no', 'username',
                                             'password').get(id=ise_id)
    except BaseException:
        pass

    if not ise_details:
        return status.HTTP_404_NOT_FOUND

    https_str = 'http' if not https else 'https'

    if ise_details.get('mrc1_status'):
        IP = ise_details.get('ip_primary')
    elif ise_details.get('mrc2_status'):
        IP = ise_details.get('ip_secondary')
    else:
        return status.HTTP_504_GATEWAY_TIMEOUT

    AUTH = (
        ise_details.get('username'),
        decryption(
            ise_details.get('password')))
    ISE_NO = ise_details.get('serial_no') + "/"

    if query:
        ARRAY_DETAIL = https_str + "://" + str(IP) + "/query/"
    else:
        ARRAYS = https_str + "://" + str(IP) + "/storage/arrays/"
        ARRAY_DETAIL = ARRAYS + ISE_NO

    return (ARRAY_DETAIL, AUTH, ise_id)


def network_ip_select(ise_id, https=True, primary=True, manual_ip=None):
    '''
    Returns url for requested ise_id.
    If primary true means we are going to change primary ip or network 1.
    If manual ip given, generates url for user-given ip.
    '''
    IP = None
    ise_details = {}

    try:
        ise_details = ListIse.objects.values('id', 'ip_primary', 'mrc1_status',
                                             'mrc2_status', 'ip_secondary',
                                             'serial_no', 'username',
                                             'password').get(id=ise_id)
    except BaseException:
        pass

    if not ise_details:
        return status.HTTP_404_NOT_FOUND

    https_str = 'http' if not https else 'https'

    IP = manual_ip
    ARRAYS = https_str + "://" + str(IP) + "/query/"

    if not manual_ip:
        if primary and ise_details.get('mrc2_status'):
            IP = ise_details.get('ip_secondary')

        if not primary and ise_details.get('mrc1_status'):
            IP = ise_details.get('ip_primary')

        ARRAYS = https_str + "://" + str(IP) + "/storage/arrays/"
    AUTH = (
        ise_details.get('username'),
        decryption(
            ise_details.get('password')))
    ISE_NO = ise_details.get('serial_no') + "/"

    return (ARRAYS + ISE_NO, AUTH, ise_id)


if __name__ == '__main__':
    pass
