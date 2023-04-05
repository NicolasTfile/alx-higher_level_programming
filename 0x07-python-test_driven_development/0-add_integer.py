#!/usr/bin/python3
""" A module containing the function add_integer() """


def add_integer(a, b=98):
    """This function returns the addition of 2 args or a raised Error
    arg a: should be an int, convert to type int if float
    arg b: should br an int, convert to type int if float
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a+b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
