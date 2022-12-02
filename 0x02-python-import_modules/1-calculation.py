#!/usr/bin/python3
from calculator import add, sub, mul, div

a = 10
b = 5


def print_calc(arg):
    sign = ''
    func = None
    if arg == "add":
        sign = '+'
        func = add
    elif arg == "sub":
        sign = '-'
        func = sub
    elif arg == "mul":
        sign = '*'
        func = mul
    elif arg == "div":
        sign = '/'
        func = div

    print(f"{a} {sign} {b} = {func(a, b)}")


if __name__ == "__main__":
    print_calc("add")
    print_calc("sub")
    print_calc("mul")
    print_calc("div")
