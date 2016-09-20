from InterviewCake.random import *

ITERATIONS = 1000000


def test_random1():
    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand7()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    print("rand7() distribution:")
    print(results)

    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand5_biased()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    print("rand5_biased() distribution:")
    print(results)

    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand5()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    print("rand5() distribution:")
    print(results)
