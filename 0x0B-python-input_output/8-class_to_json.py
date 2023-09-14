#!/usr/bin/python3
"""returns a dictionary discription"""


def class_to_json(obj):
    """returns a dictionary discription"""
    if type(obj.__class__) is type:
        return obj.__dict__
