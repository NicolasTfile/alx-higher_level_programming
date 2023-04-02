#!/usr/bin/python3
""" Module that contains the function print_square() """


def print_square(size):
    """ Prints a square with the # char
    Args:
        size: the size of the square we ant printed
    Return: no return
    """
    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
