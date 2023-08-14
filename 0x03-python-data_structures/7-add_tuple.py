#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    c = (0 if len(a) < 1 else a[0]) + (0 if len(b) < 1 else b[0])
    d = (0 if len(a) < 2 else a[1]) + (0 if len(b) < 2 else b[1])
    return (c, d)
