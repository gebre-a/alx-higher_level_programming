#!/usr/bin/python3
"""module with lookup method"""


def lookup(obj):
    """lookup method function
    Returns: a list of available attributes and methods of an object"""
    return dir(obj)
