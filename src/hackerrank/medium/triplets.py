#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    # O(n)
    triplets = {}
    for an in arr:
        if an in triplets:
            triplets[an]['n1_count'] += 1
        else:
            triplets[an] = {
                'n1_count': 1,      # an = a*r**(n-1) = a*r**(1-1) = a*r**(0) = a*1 = a
                'n2_count': 0,      # an = a*r**(n-1) = a*r**(2-1) = a*r**(1) = a*r; a = an/r
                'n3_count': 0,      # an = a*r**(n-1) = a*r**(3-1) = a*r**(2) = a*r**2; a = an/(r**2)
                }

        a2 = an / r
        a3 = an / (r ** 2)
        if a2 in triplets:
            triplets[a2]['n2_count'] += 1
            if a2 == an:
                if triplets[a2]['n2_count'] == 1:
                    triplets[an]['n1_count'] -= 1
                else:
                    triplets[a2]['n2_count'] -= 1
        if a3 in triplets:
            triplets[a3]['n3_count'] += 1
            if a3 == an:
                if triplets[a3]['n3_count'] == 1:
                    triplets[an]['n1_count'] -= 1
                else:
                    triplets[a3]['n3_count'] -= 1

    # O(n)
    # Visit all potential triplets and count the ones that make up actual geometric series
    result = 0
    for a, triplet in triplets.items():
        result += (triplet['n1_count'] * triplet['n2_count'] * triplet['n3_count'])

    # Big O = O(n) + O(n) = O(2n) = O(n)
    return result
