#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """a class that inherits from int"""
    def __eq__(self, other):
        """inverts eq to ne"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts ne to eq"""
        return super().__eq__(other)
