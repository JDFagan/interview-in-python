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
    # print(f"Evaluating geometric for array: {arr}, r = {r}")
    # # a_{n}=a\,r^{n-1}.
    for n, num in enumerate(arr, start=1):
        # print(f"num != a*r**(n - 1): {num} != {a}*{r}**({n}-1) -> {num} != {a}*{r**(n-1)} -> {num} != {a*r**(n - 1)} -> {num != a*r**(n - 1)}")
        if num != a*r**(n - 1):
            return False
    return True


# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0

    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if is_geometric([arr[i], arr[j], arr[k]], r):
                    result += 1

    return result


input = [1, 2, 2, 4]
geometric_triplets = countTriplets(input, 2)
print(geometric_triplets)

input = [1, 3, 9, 9, 27, 81]
geometric_triplets = countTriplets(input, 3)
print(geometric_triplets)

input = [1, 883159100, 531288700, 190057300, 151290300, 718720100, 402786700, 289690000, 492421700, 35732600, 918678200, 9109700, 679750500, 78252800, 316415300, 587749600, 350835900, 665426700, 767120400, 529309500, 130034100, 492039900, 23386800, 194100900, 637764700, 284555300, 755330400, 309556600, 325711300, 929440600, 627497900, 35557300, 507791300, 771392800, 308196000, 281129700, 741852000, 494288900, 436822400, 553091300, 977066400, 517986200, 410654400, 231572100, 365522700, 995936300, 148703700, 278852800, 476615100, 872867200, 262131100, 242785700, 439300000, 74010600, 731626000, 197219200, 582995400, 821584400, 929335400, 430854900, 138539800, 233465700, 625984200, 690654500, 615522600, 581559300, 849803800, 312728000, 440556300, 400676300, 703000700, 69661600, 224160600, 664785000, 585747400, 84358000, 865252500, 556686200, 141397700, 479225400, 18557400, 910220000, 277198700, 874613900, 302874600, 135221100, 515683100, 6723500, 22034700, 653911200, 929303700, 556004300, 413500700, 220252900, 895411100, 893413400, 451605200, 191768600, 483506200, 240281100, 119270300, 11207000, 936235700, 1971590]
geometric_triplets = countTriplets(input, 100)
print(geometric_triplets)
