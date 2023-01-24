#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    function that divides element by element 2 lists.
    """

    for i in range(list_lenght):
        try:
            div = my_list_1[i] / my_list_2[i]
            #new_list.append(div)
        except IndexError:
            print("out of range")
            div = 0
            #new_list.append(0)
        except ZeroDivisionError:
            print("division by zero")
            div = 0
            #new_list.append(0)
        except TypeError:
            print("wrong type")
            div = 0
            #new_list.append(0)
        finally:
            new_list.append(div)
    return new_list
