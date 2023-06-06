#!/usr/bin/python3
# checks the values of a, b, and c and performs different operations
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
