#!/usr/bin/python3
"""returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    if my_obj:
        data = json.dumps(my_obj)
        return data
