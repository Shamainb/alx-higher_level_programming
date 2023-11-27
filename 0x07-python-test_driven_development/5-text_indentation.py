#!/usr/bin/python3
"""The module contains a function that
    adds two newlines to ".?:" and
    prints the text, one line after the
    other
    """


def text_indentation(text):
    """This function does as explained in the module section
    Args:
        text(str): The text to print
    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print()
        return
    text = text.replace(".", ".\n\n").replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    lines = text.split("\n")
    for line in range(len(lines)):
        if line == 0:
            print("{}".format((lines[line]).strip()), end="")
        else:
            print("\n{}".format((lines[line]).strip()), end="")
