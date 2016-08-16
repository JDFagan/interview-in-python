from InterviewCake.highest_product import *
import pytest


def test_sort1():
    ints = [1, 2, 3, 4]
    assert sort_high_to_low(integers=ints) == [4, 3, 2, 1]


def test_sort2():
    ints = [-10, -10, 1, 3, 2]
    assert sort_high_to_low(integers=ints) == [3, 2, 1, -10, -10]


def test_1():
    ints = [1, 2, 3, 4]
    assert get_highest_product(integers=ints) == 4*3*2


def test_2():
    ints = [1, 2, 3, 4, 5]
    assert get_highest_product(integers=ints) == 5*4*3


def test_3():
    ints = [22, -5, 2, 3333, 45, 10]
    assert get_highest_product(integers=ints) == 3333*45*22


def test_4():
    ints = [7, 3, 4]
    assert get_highest_product(integers=ints) == 7*3*4


def test_negatives():
    ints = [-10, -10, 1, 3, 2]
    assert get_highest_product(integers=ints) == -10*-10*3


def test_zeroes():
    ints = [0, 0, 0]
    assert get_highest_product(integers=ints) == 0


def test_two_elements():
    with pytest.raises(IndexError):
        ints = [7, 3]
        get_highest_product(integers=ints)


def test_one_element():
    with pytest.raises(IndexError):
        ints = [7]
        get_highest_product(integers=ints)


def test_no_elements():
    with pytest.raises(IndexError):
        ints = []
        get_highest_product(integers=ints)
