from InterviewCake.random import *
import time

ITERATIONS = 1000000


def __test_randomX(fn):
    t0 = time.time()
    results = {}
    i = 0
    while i < ITERATIONS:
        result = fn()
        if result in results:
            results[result] += 1
        else:
            results[result] = 1
        i += 1
    t1 = time.time()
    print("{}() distribution:".format(fn))
    print(results)
    print("time: {}".format(t1 - t0))
    print()


def test_random5():
    __test_randomX(rand7)
    __test_randomX(rand5_biased)
    __test_randomX(rand5_cake)
    __test_randomX(rand5_die)


def test_random7():
    __test_randomX(rand5)
    __test_randomX(rand7_biased)
    __test_randomX(rand7_cake)
    __test_randomX(rand7_die)
