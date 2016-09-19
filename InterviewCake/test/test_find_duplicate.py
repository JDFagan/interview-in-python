from InterviewCake.find_duplicate import *


def test_no_elements():
    numbers = []
    assert find_duplicate_number(numbers) is None


def test_one_elements():
    numbers = [1]
    assert find_duplicate_number(numbers) is None


def test_dup0():
    numbers = [1, 2, 3]
    assert find_duplicate_number(numbers) is None


def test_dup1():
    numbers = [1, 2, 3, 4, 3]
    assert find_duplicate_number(numbers) == 3


def test_dup2():
    numbers = [2, 1, -10, 0, 1]
    assert find_duplicate_number(numbers) == 1
