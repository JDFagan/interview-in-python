from InterviewCake.random import *
import time

ITERATIONS = 1000000


def test_random5():
    t0 = time.time()
    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand7()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    t1 = time.time()
    print("rand7() distribution:")
    print(results)
    print("time: {}".format(t1 - t0))
    print()

    t0 = time.time()
    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand5_biased()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    t1 = time.time()
    print("rand5_biased() distribution:")
    print(results)
    print("time: {}".format(t1 - t0))
    print()

    t0 = time.time()
    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand5_cake()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    t1 = time.time()
    print("rand5_cake() distribution:")
    print(results)
    print("time: {}".format(t1 - t0))
    print()

    t0 = time.time()
    results = {}
    i = 0
    while i < ITERATIONS:
        result = rand5_die()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    t1 = time.time()
    print("rand5_die() distribution:")
    print(results)
    print("time: {}".format(t1 - t0))
    print()
