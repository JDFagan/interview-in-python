#!/bin/python3

import math
import os
import random
import re
import sys


def is_anagram(s1: str, s2: str):
    return sorted(s1) == sorted(s2)


def get_substrings(s: str):
    return [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]


# def get_subsequences(s: str):
#     return [''.join(combo) for n in range(1, len(s)) for combo in itertools.combinations(s, n)]


def sherlockAndAnagrams(s):
    # O(n)
    substrings = get_substrings(s)

    # O(ss)
    # Map of the unique lengths of all substrings
    substring_lengths = {}
    for substring in substrings:
        substring_length = len(substring)
        if substring_length in substring_lengths:
            substring_lengths[substring_length].append(substring)
        else:
            substring_lengths[substring_length] = [substring]
    print(f"substring_lengths = {substring_lengths}")

    # O(ss)
    # Filter out those substrings for each unique length that match another pair anagram wise
    # anagrams = []
    anagrams = []
    for substring_length, substrings in substring_lengths.items():
        print(f"{substring_length}: {substrings}")
        for i, ss1 in enumerate(substrings):
            # print(f"(i = {i}): st = {ss1}")
            for j, ss2 in enumerate(substrings[i+1:]):
                # print(f"(j = {j}) ss = {ss2}")
                if is_anagram(ss1, ss2):
                    # anagrams += [[i, j+1]]
                    anagrams += [[ss1, ss2]]

            # anagrams += [[substring_list, ss] for ss in [substring_lists[i:]] if is_anagram(substring_list, ss)]
            # print(f"anagrams = {anagrams}")

    # Brute force: O(n**2)
    # anagrams = [[ss1, ss2] for i, ss1 in enumerate(substrings) for ss2 in substrings[i+1:] if is_anagram(ss1, ss2)]
    print(anagrams)

    # Total O = O(n + 2ss) = O(n + ss)
    return len(anagrams)
