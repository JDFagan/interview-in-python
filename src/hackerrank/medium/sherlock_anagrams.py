#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


def is_anagram(s1: str, s2: str):
    return sorted(s1) == sorted(s2)


def get_substrings(s: str):
    return [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]


# def get_subsequences(s: str):
#     return [''.join(combo) for n in range(1, len(s)) for combo in itertools.combinations(s, n)]


def sherlockAndAnagrams(s):
    # Get all substrings of string s
    substrings = get_substrings(s)

    anagrams = []
    for i, ss1 in enumerate(substrings):
        for ss2 in substrings[i+1:]:
            if is_anagram(ss1, ss2):
                anagrams.append([ss1, ss2])

    print(anagrams)
    return anagrams
