#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_ = 0
    for i in set(my_list):
        sum_ += i
    return sum_
