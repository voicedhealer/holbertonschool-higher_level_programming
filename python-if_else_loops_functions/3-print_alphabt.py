#!/usr/bin/python3

for alpha in range(97, 123):
    if chr(alpha) == chr(101) or chr(113):
        continue
        print("{}".format(chr(alpha)), end="")
