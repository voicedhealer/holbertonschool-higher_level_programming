#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Déterminer les deux valeurs pertinentes pour tuple_a
    if len(tuple_a) == 0:
        val1_a = 0
        val2_a = 0
    elif len(tuple_a) == 1:
        val1_a = tuple_a[0]
        val2_a = 0
    else:
        val1_a = tuple_a[0]
        val2_a = tuple_a[1]

    # Déterminer les deux valeurs pertinentes pour tuple_b
    if len(tuple_b) == 0:
        val1_b = 0
        val2_b = 0
    elif len(tuple_b) == 1:
        val1_b = tuple_b[0]
        val2_b = 0
    else:
        val1_b = tuple_b[0]
        val2_b = tuple_b[1]

    result1 = val1_a + val1_b
    result2 = val2_a + val2_b
    # Retourner le nouveau tuple
    return (result1, result2)
