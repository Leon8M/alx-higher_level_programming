#!/usr/bin/python3
# prints last digit of a number
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
