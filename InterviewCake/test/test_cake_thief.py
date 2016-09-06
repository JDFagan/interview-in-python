from InterviewCake.cake_thief import *


def test_no_elements():
    cake_tuples = []
    capacity = 20
    assert max_duffel_bag_value(cake_tuples, capacity) == 0


def test_thief1():
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity = 20
    assert max_duffel_bag_value(cake_tuples, capacity) == 555


def test_thief2():
    cake_tuples = [(1, 30), (50, 200)]
    capacity = 100
    assert max_duffel_bag_value(cake_tuples, capacity) == 3000
