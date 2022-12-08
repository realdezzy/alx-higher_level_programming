#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numr = 0
    demr = 0
    for x in my_list:
        numr += (x[0] * x[1])
        demr += x[1]

    return numr / demr
