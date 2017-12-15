import sys
import json
import xmltodict
import os.path


def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

if not len(sys.argv) == 3:
    print "\nError: Give proper filename\nExample: python compile.py input.xml output.json\n"
    sys.exit()

fn_json = sys.argv[2] if ((sys.argv[2].split(".")[1]) == "json") else False 
ifn_xml = sys.argv[1] if ((sys.argv[1].split(".")[1]) == "xml") else False

if fn_json and ifn_xml:
    if not os.path.exists(ifn_xml):
        print ("%s File not exists" % (ifn_xml))
        sys.exit()
    with open(fn_json, "wb") as fb:
        data = convert(ifn_xml)
        fb.write(data)
        print "%s File created" % (fn_json) 
else:
    print "Error: Invalid file extension - ", sys.argv[1], sys.argv[2]