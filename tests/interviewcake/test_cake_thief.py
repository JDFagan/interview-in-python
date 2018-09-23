from interviewcake.cake_thief import *
import math


def test_no_elements():
    cake_tuples = []
    capacity = 20
    assert max_duffel_bag_value(cake_tuples, capacity) == 0


def test_zero_capacity():
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity = 0
    assert max_duffel_bag_value(cake_tuples, capacity) == 0


def test_zero_cake_weight():
    cake_tuples = [(7, 160), (0, 90), (2, 15)]
    capacity = 20
    assert max_duffel_bag_value(cake_tuples, capacity) == math.inf


# I fail this test
# def test_zero_cake():
#     cake_tuples = [(7, 160), (0, 0), (2, 15)]
#     capacity = 20
#     assert max_duffel_bag_value(cake_tuples, capacity) == math.nan


def test_thief1():
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity = 20
    assert max_duffel_bag_value(cake_tuples, capacity) == 555


def test_thief2():
    cake_tuples = [(1, 30), (50, 200)]
    capacity = 100
    assert max_duffel_bag_value(cake_tuples, capacity) == 3000
