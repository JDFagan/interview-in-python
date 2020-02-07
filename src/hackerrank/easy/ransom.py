#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine: [str], note: [str]):
    magazine_words = {}
    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    for word in note:
        if word not in magazine_words:
            print("No")
            return
        else:
            if magazine_words[word] == 1:
                magazine_words.pop(word)
            else:
                magazine_words[word] -= 1

    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
