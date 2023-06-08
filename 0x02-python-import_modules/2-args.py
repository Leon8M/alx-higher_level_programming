#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num = len(args)
    print("{}".format(num), end=" ")
    if num == 1:
        print("argument:")
    elif num == 0:
        print("arguments.")
    else:
        print("arguments:")
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
