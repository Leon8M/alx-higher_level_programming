#!/usr/bin/python3
# prints the ASCII alphabet in reverse alternating lowercase and uppercase
for i in range(ord('z'), ord('a') - 1, -1):
    num = ''
    letter = chr(i)
    if i % 2 == 0:
        num = letter.lower()
    else:
        num = letter.upper()
    print("{}".format(num), end='')
