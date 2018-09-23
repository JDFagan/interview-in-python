#!/bin/python3

import math
import os
import random
import re
import sys


def max_difference(ints):
    result = -1
    new_max_result = -1
    n = len(ints)
    max_value = None
    for i in range(1, n):
        if max_value is None:
            max_value = ints[i]
        elif ints[i] > max_value:
            delta_new_max = ints[i] - max_value
            max_value = ints[i]
            new_max_result = result + delta_new_max
        diff = ints[i] - ints[i - 1]
        result = max(result, new_max_result, diff)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    res = max_difference(ints=a)
    print("result = {}".format(res))

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
