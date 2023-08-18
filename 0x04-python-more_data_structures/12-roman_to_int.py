#!/usr/bin/python3

def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    # create a dictionary conv to hold roman numerals key, value pairs e.g I=1
    conv = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    # initialize a variable sum_ and tmp to zero
    sum_ = 0
    tmp_v = 0

    # convert roman string to list and reverse it and loop through it
    for i in reversed(list(roman_string)):

        # loop through conv to compare roman string index and conv key
        for k, v in conv.items():
            if k == i and v >= tmp_v:
                # add value of roman string index to variable sum_
                tmp_v = v
                sum_ += v
                break
            # if value of next roman index is less than the conv key value
            elif k == i and v < tmp_v:
                # subtract value of roman string from variable sum_
                sum_ -= v
                tmp_v = v
                break

    # return sum_
    return sum_
