#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        numbers_string = []        
    for numbers in row:
        numbers_format = "{:d}".format(numbers)
        numbers_string.append(numbers_format)
    line_print = " ".join(numbers_string)
    print(line_print)
