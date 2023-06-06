#!/usr/bin/python3
# checks for lowercase character
def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
