#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    result = []
    while index is not list_length:
        try:
            result.append(my_list_1[index] / my_list_2[index])
            index += 1
        except TypeError:
            result.append(0)
            index += 1
            print("wrong type")
        except ZeroDivisionError:
            result.append(0)
            index += 1
            print("division by 0")
        except IndexError:
            result.append(0)
            index += 1
            print("out of range")
        finally:
            None
    return result
