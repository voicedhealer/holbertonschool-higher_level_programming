#!/usr/bin/python3
def multiple_returns(sentence):
    len_char = len(sentence)

    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]

    return(len_char,first_char)
