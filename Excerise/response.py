import requests 
import xml.dom.minidom
import json

r = requests.get("http://10.20.238.4/storage/arrays/USE2600053GOI05C",auth=('administrator', 'administrator'))

xmlstring = r.text
xml = xml.dom.minidom.parseString(xmlstring) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
print xml
print pretty_xml_as_string
print pretty_xml_as_string.json


