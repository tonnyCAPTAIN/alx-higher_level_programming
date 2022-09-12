#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x is not None:
             for val in range(0, x):
                 print("{}".format(my_list[val]), end="")
             print()
             return x
    except (IndexError):
        print()
        return val
