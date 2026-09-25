#!/usr/bin/env python3
"""Module that provides XML serialization and deserialization functions."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Read an XML file and return a deserialized Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: The reconstructed Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result
    except Exception:
        return None
