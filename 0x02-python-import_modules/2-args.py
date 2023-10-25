#!/usr/bin/python3

from sys import argv, exit
if __name__ == "__main__":
    num = len(argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
        exit(0)
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))

    for i in range(1, num):
        print("{}: {}".format(i, argv[i]))
