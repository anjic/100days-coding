RESOURCE = {
    'volumes': 'volumes',
    'hosts': 'hosts',
    'endpoints': 'endpoints',
    'allocations': 'allocations',
    'pools': 'pools',
    'mirrors': 'mirrors',
    'drives': 'drives',
    'files': 'files',
    'snmp': 'snmp',
    'subscriptions': 'subscriptions',
    'performance': 'performance',
    'chronometer': 'chronometer',
    'controllers': 'controllers',
    'powersupplies': 'powersupplies',
    'media': 'media',
    'datareduction': 'datareduction',
    'network': 'network',
    'batteries': 'batteries',
    'fans': 'fans',
    'encryption': 'encryption',
    'fcports': 'fcports'
}

AUTH = ("administrator", "administrator")

HEADER_JSON = {
    "Content-Type": "application/xml"
}

HEADER_XML = {
    "Content-Type": "application/xml"
}

HEADER_TEXT = {
    "Content-Type": "plain/text"
}
# influx db configuration

INFLUX_USER = 'root'
INFLUX_PASSWORD = 'password'
INFLUX_DBNAME = 'xio_metric'
INFLUX_HOST = 'localhost'
INFLUX_PORT = 8086
ISE_ID = '3DE100RT'

# Socket Configuration

SOCKET_IP = '127.0.0.1'
SOCKET_PORT = 5000
WS_PORT = 9999
WSS = True

# redis db configuration

RDS_DB = 0
RDS_HOST = 'localhost'
RDS_PORT = 6379

# scripts TimeInterval
TimeInterval = 30

# ise status code
ISE_STATUS_CODE = {
    'running': 0,
    'warning': 1,
    'reformat': 2,
    'initialize': 3,
    'restart': 4,
    'shutdown': 5
}

ISE_STATUS = {
    "running": False,
    "reformat": False,
    "initialize": False,
    "shutdown": False,
    "restart": False,
    "identify": False

}
# JWT secret Key
secret = 'qwertyuiopasdfghjklzxcvbnm123456'
encryption_key = '00112233445566778899AABBCCDDEEFF'

ARRAYCHART = {
    'readiops' : 'Read IOPS',
    'writeiops' : 'Write IOPS',
    'totaliops' : 'Total IOPS',
    'readkbps' : 'Read KB/s',
    'writekbps' : 'Write KB/s',
    'totalkbps' : 'Total KB/s',
    'readlatency':'Read Latency',
    'writelatency':'Write Latency',
    'queuedepth':'Queue Depth'
}