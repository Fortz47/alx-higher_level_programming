#!/usr/bin/python3
class TooFarException(Exception):
    pass
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise TooFarException('Too far')
            result = result + (a ** b / i)
        except TooFarException:
            result = result + (b + a)
    return result
