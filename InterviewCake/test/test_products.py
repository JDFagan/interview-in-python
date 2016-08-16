from InterviewCake.products import get_products_of_all_ints_except_at_index
import pytest


def test_1():
    ints = [1, 7, 3, 4]
    assert get_products_of_all_ints_except_at_index(integers=ints) == [84, 12, 28, 21]


def test_2():
    ints = [7, 3, 4]
    assert get_products_of_all_ints_except_at_index(integers=ints) == [12, 28, 21]


def test_zeroes():
    ints = [0, 0, 0]
    assert get_products_of_all_ints_except_at_index(integers=ints) == [0, 0, 0]


def test_two_elements():
    ints = [7, 3]
    assert get_products_of_all_ints_except_at_index(integers=ints) == [3, 7]


def test_one_element():
    ints = [7]
    assert get_products_of_all_ints_except_at_index(integers=ints) == [None]


def test_no_elements():
    with pytest.raises(IndexError):
        ints = []
        get_products_of_all_ints_except_at_index(integers=ints)
