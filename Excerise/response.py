import requests 
from requests.auth import HTTPBasicAuth
#from excerise import xmltojson

r = requests.get("http://10.20.238.4/storage/arrays/USE2600053GOI05C",auth=HTTPBasicAuth('administrator', 'administrator'))

print (r.text)
#print (r.json())