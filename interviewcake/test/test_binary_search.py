from interviewcake.binary_search import *


def test_no_elements():
    nums = []
    assert not binary_search(70, nums)
    assert not binary_search(None, nums)
    assert not binary_search([], nums)


def test_search1():
    nums = [67, 68, 68, 68, 69, 70, 71]
    assert binary_search(70, nums)
    assert not binary_search(90, nums)


def test_search2():
    nums = [67, 68, 68, 68, 69, 70, 71]
    assert binary_search(67, nums)
    assert binary_search(71, nums)
    assert binary_search(68, nums)
    assert binary_search(69, nums)
    assert not binary_search(60, nums)
    assert not binary_search(72, nums)
