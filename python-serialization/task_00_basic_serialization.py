#!/usr/bin/env python3
"""Module that provides basic JSON serialization and deserialization functions.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
