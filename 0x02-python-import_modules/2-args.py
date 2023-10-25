#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of  and arguments."""
import sys

num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 argument.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
