#!/usr/bin/python3
# all possible different smallest combinations of two unlike digits
for num1 in range(10):
    for num2 in range(10):
        if (num1 != num2) and (num1 < num2):
            print("{}{},".format(num1, num2), end=" ")
