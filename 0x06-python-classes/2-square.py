#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that describes properties of square.

        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
