#!/usr/bin/python3
from sys import argv, exit
import calculator_1 as cal
if __name__ == "__main__":
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+' or op == '-' or op == '*' or op == '/':
        if op == '+':
            n = cal.add(a, b)
        elif op == '-':
            n = cal.sub(a, b)
        elif op == '*':
            n = cal.mul(a, b)
        elif op == '/':
            n = cal.div(a, b)
        print("{} {} {} = {}".format(a, op, b, n))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
