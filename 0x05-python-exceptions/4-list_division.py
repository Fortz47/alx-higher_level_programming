#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]

            # Check for division by zero
            if value_2 == 0:
                raise ZeroDivisionError('division by 0')

            # Check if values are numeric
            if not isinstance(value_1, (int, float))
                raise TypeError('wrong type')

            if not isinstance(value_2, (int, float)):
                raise TypeError('wrong type')

            # Perform division and append result to the result list
            division_result = value_1 / value_2
            result.append(division_result)

        except IndexError:
            print('out of range')
            result.append(0)
        except ZeroDivisionError:
            print('division by 0')
            result.append(0)
        except TypeError:
            print('wrong type')
            result.append(0)
        finally:
            pass  # The finally block is executed regardless of exceptions

    return result
