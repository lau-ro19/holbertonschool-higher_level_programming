#!/usr/bin/env python3
"""Module that provides a custom class with pickle serialization methods."""
import pickle


class CustomObject:
    """A custom class to demonstrate object serialization using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and is_student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes with a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Args:
            filename (str): The filename to save the pickled object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The filename of the pickled file.

        Returns:
            CustomObject or None: The deserialized instance, or None on error.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
