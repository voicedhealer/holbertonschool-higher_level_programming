#!/usr/bin/python3
"""
Module pour sérialiser et désérialiser un
dictionnaire Python en XML et inversement.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML
    et l'enregistre dans le fichier donné.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
