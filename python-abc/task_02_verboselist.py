#!/usr/bin/python3
"""
class VerboseList
"""
from typing import SupportsIndex


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, add_iterable):
        num_items_to_add = len(add_iterable)
        super().extend(add_iterable)
        print(f"Extended the list with {num_items_to_add} items")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index: SupportsIndex = -1):
        element_remove = self[index]
        print(f"Popped {element_remove} from the list.")
        return super().pop(index)
