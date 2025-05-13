#!/usr/bin/python3
def no_c(my_string):
    nouvelle_chaine = ""
    for caractere in my_string:
        if caractere != 'c' and caractere != 'C':
         nouvelle_chaine += caractere
    return nouvelle_chaine
