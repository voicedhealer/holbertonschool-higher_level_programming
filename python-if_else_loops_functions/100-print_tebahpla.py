#!/usr/bin/python3
# Ce script affiche l'alphabet en ordre inversé, alternant maj/min.

# Boucle de ord('z') à ord('a')
for i in range(ord('z'), ord('a') - 1, -1):
    # Version avec une expression conditionnelle plus directe :
    print("{}".format(chr(i - 32) if i % 2 != 0 else chr(i)), end="")
