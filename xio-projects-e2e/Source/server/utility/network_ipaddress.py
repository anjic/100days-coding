import subprocess


def ip_ping(ip):
    '''
    This is for checking the status of ISE IP. It returns True or False based on IP status.
    '''
    if ip:
        ip_response = subprocess.Popen(['ping',
                                        (ip),
                                        '-c',
                                        '6',
                                        "-W",
                                        "6"],
                                       shell=False,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
        ip_response.wait()
        ip_status = True if ip_response.poll() == 0 else False
        return ip_status
