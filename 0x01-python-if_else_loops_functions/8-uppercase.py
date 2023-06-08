#!/usr/bin/python3
# prints a string in uppercase followed by a new line
def uppercase(str):
    upper = ''
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper += chr(ord(char) - 32)
        else:
            upper += char
    print("{}".format(upper))
