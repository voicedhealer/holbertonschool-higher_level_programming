#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    copied_list = my_list[:]
    if idx < 0:
        return copied_list
    if idx >= len(my_list):
        return copied_list

    copied_list[idx] = element
    return copied_list
