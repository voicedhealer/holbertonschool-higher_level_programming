#!/usr/bin/python3

for alpha in range(97, 123):
    if alpha not in [101, 113]:
        print("{}".format(chr(alpha)), end="")
