#!/usr/bin/python3
def uniq_add(my_list=[]):
    res_list = []
    res = 0
    for integer in my_list:
        if integer not in res_list:
            res_list.append(integer)
    for uniqno in res_list:
        res += uniqno
    return res
