#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    length = []
    while count < list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            count += 1
            length.append(result)
    return length
