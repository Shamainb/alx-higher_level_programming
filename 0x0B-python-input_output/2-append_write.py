#!/usr/bin/python3
"""append_write: appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
     Appends a string at the end of a text file
      returns the number of characters added
      Args:
      filename: the text file
      text: to be appended
      Return: number of characters added
      """
      with open(filename, 'a', encoding='UTF8') as file:
          num_char_appended = file.append(text)
          return(num_char_appended)
