#!/usr/bin/python3
"""read_file: reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    Args:
    filename: the file we are reading and print
    """
    with open(filename, encoding="UTF8") as file:
        content = file.read()
        print(content)
        file.closed
