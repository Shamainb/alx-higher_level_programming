#!/usr/bin/python3
"""write_file: writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    returns the number of characters written
    Args:
    filename:  writes a string to a text file (UTF8)
    Return: number of characters written
    """
    with open(filename, 'w', encoding='UTF8') as file:
        num_char_written = file.write(text)
        return(num_char_written)
