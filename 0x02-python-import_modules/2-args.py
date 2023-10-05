#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    def main():

        num_args = len(sys.argv) - 1

        if num_args == 0:
            print("0 argument.")
        elif num_args == 1:
            print("1 argument:")
        else:
            print(f"{num_args} arguments:")

            if num_args > 0:
                for i in range(1, num_args + 1):
                    print(f"{i}: {sys.argv[i]}")
            else:
                print(".")