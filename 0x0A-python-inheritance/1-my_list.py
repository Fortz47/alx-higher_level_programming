#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list in ascendimg order"""
        sorted_list = sorted(self)
        print(sorted_list)