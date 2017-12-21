from lxml import objectify
import re
from json import dumps
import requests


def flatten_attributes(property_name, lookup, attributes):
    '''This converts each xml element to json and returns it'''
    if attributes is None:
        return lookup

    if not isinstance(lookup, dict):
        return dict(attributes.items() + [(property_name, lookup)])

    return dict(lookup.items() + attributes.items())


def xml_element_to_json(xml_element, attributes):
    '''This converts datatype of the xml elements'''
    if isinstance(xml_element, objectify.BoolElement):
        return flatten_attributes(
            xml_element.tag,
            bool(xml_element),
            attributes)

    if isinstance(xml_element, objectify.IntElement):
        if len(str(xml_element.text)) >= 15:
            return flatten_attributes(
                xml_element.tag, str(
                    xml_element.text), attributes)
        return flatten_attributes(
            xml_element.tag,
            int(xml_element),
            attributes)

    if isinstance(xml_element, objectify.FloatElement):
        return flatten_attributes(
            xml_element.tag, str(
                xml_element.text), attributes)

    if isinstance(xml_element, objectify.StringElement):
        return flatten_attributes(
            xml_element.tag,
            str(xml_element).strip(),
            attributes)

    return flatten_attributes(
        xml_element.tag,
        convert_xml_to_json(
            xml_element.getchildren()),
        attributes)


def convert_xml_to_json(xml_object):
    '''This is for conversion of xml to json.It converts and returns each xml tag to dictionary'''
    attributes = None
    if hasattr(xml_object, "attrib") and not xml_object.attrib == {}:
        attributes = dict(_attr=dict(xml_object.attrib))

    if isinstance(xml_object, objectify.ObjectifiedElement):
        return xml_element_to_json(xml_object, attributes)

    if isinstance(xml_object, list):
        if len(xml_object) > 1 and all(
                xml_object[0].tag == item.tag for item in xml_object):
            return [convert_xml_to_json(attr) for attr in xml_object]

        return dict([(item.tag, convert_xml_to_json(item))
                     for item in xml_object])

    return Exception("Not a valid lxml object")


def xml_to_json(xml):
    '''This is for conversion of xml to json. It returns JSON object'''
    xml = re.sub('[&]', '', xml)
    xml_object = xml if isinstance(xml, objectify.ObjectifiedElement) \
        else objectify.fromstring(xml)
    return dumps({xml_object.tag: convert_xml_to_json(xml_object)})


if __name__ == '__main__':
    pass
