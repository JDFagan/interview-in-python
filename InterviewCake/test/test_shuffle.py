from InterviewCake.shuffle import *


def test_shuffle0():
    items = [1, 1, 1]
    assert shuffle_inplace(items) == [1, 1, 1]


def test_shuffle1():
    items = [1, 2, 3, 4, 5, 6, 7]
    assert shuffle_inplace(items) != [1, 2, 3, 4, 5, 6, 7]


def test_shuffle2():
    items = [1, 2, 1, 4, 5, 6, 7]
    assert shuffle_inplace(items) != [1, 2, 1, 4, 5, 6, 7]
