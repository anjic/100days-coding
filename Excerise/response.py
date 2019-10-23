import requests 
import xml.dom.minidom
import json

r = requests.get("https://udstest.udsdomain.com/ovirt-engine/api",auth=('admin', 'ovirt123'))
print r.text
# xmlstring = r.text
# xml = xml.dom.minidom.parseString(xmlstring) # or xml.dom.minidom.parseString(xml_string)
# pretty_xml_as_string = xml.toprettyxml()
# print xml
# print pretty_xml_as_string
# print pretty_xml_as_string.json


