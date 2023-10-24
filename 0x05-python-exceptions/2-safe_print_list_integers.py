#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers
    Args:
    my_list (list): The list of elements
    x (int): The number of elements in my_list
    Returns:
    The number to be printed
    """

    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = + 1
        except (ValueError, TypeError):
            continue
        print("")
        return (count)
