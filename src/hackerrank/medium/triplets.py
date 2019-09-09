#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0

    counts   = {}
    potentials = {}
    for an in arr:
        a2 = an / r
        a3 = an / (r ** 2)

        if a3 in potentials:
            potentials[a3] += 1
            result +=
            for a3_map in triplets[a3]:
                a3_map['n3_count'] += 1
                result += a3_map['n2_count']
        if a2 in triplets:
            for a2_map in triplets[a2]:
                a2_map['n2_count'] += 1

        potentials[an]
        if an in triplets:
            triplets[an].append({
                'n2_count': 0,      # an = a*r**(n-1) = a*r**(2-1) = a*r**(1) = a*r; a = an/r
                'n3_count': 0,      # an = a*r**(n-1) = a*r**(3-1) = a*r**(2) = a*r**2; a = an/(r**2)
                })
        else:
            triplets[an] = [{
                'n2_count': 0,      # an = a*r**(n-1) = a*r**(2-1) = a*r**(1) = a*r; a = an/r
                'n3_count': 0,      # an = a*r**(n-1) = a*r**(3-1) = a*r**(2) = a*r**2; a = an/(r**2)
                }]
    return result
