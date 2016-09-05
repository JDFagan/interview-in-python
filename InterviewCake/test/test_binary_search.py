from InterviewCake.binary_search import *


def test_no_elements():
    nums = []
    assert not binary_search(70, nums)
    assert not binary_search(None, nums)
    assert not binary_search([], nums)


def test_search1():
    nums = [67, 68, 68, 68, 69, 70, 71]
    assert binary_search(70, nums)
    assert not binary_search(90, nums)
