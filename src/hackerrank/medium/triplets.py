#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


def get_subsequences(a: [], seq_len=0):
    return [combo for n in range(1, len(a)) for combo in itertools.combinations(a, n) if len(combo) == seq_len]


def is_geometric(arr, r) -> bool:
    """
    :param arr: Array of numbers to see if they are in a geometric sequence
    :param r: Common ratio in a geometric sequence
    :return: bool
    """
    if r == 0:
        raise ValueError("r cannot be 0")
    if len(arr) == 0:
        return False
    a = arr[0]
    print(f"Evaluating geometric for array: {arr}, r = {r}")
    # a_{n}=a\,r^{n-1}.
    for n, num in enumerate(arr, start=1):
        print(f"num != a*r**(n - 1): {num} != {a}*{r}**({n}-1) -> {num} != {a}*{r**(n-1)} -> {num} != {a*r**(n - 1)} -> {num != a*r**(n - 1)}")
        if num != a*r**(n - 1):
            return False
    return True


# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0
    triplets = get_subsequences(arr, seq_len=3)
    for triplet in triplets:
        if is_geometric(triplet, r):
            result += 1
    print(triplets)
    return result


geometric_triplets = countTriplets([1, 2, 2, 4], 2)
print(geometric_triplets)

geometric_triplets = countTriplets([1, 3, 9, 9, 27, 81], 3)
print(geometric_triplets)
