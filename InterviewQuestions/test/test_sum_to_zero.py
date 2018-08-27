from InterviewQuestions.sum_to_zero import *


def test_sum0():
    nums = []
    assert not get_three_that_sum_to_zero(nums)
    assert not get_all_threes_that_sum_to_zero(nums)


def test_sum1():
    nums = [1, 1, -2]
    assert get_three_that_sum_to_zero(nums) == [1, 1, -2]
    assert get_all_threes_that_sum_to_zero(nums) == [(1, 1, -2)]


def test_sum2():
    nums = [1, 50, 1, 25, -2]
    assert get_three_that_sum_to_zero(nums) == [1, 1, -2]
    assert get_all_threes_that_sum_to_zero(nums) == [(1, 1, -2)]


def test_sum3():
    nums = [12, 50, 1, 25, -2]
    assert get_three_that_sum_to_zero(nums) is None
    assert get_all_threes_that_sum_to_zero(nums) == []


def test_sum4():
    nums = [12, 50, 1, 25, -2]
    assert not get_three_that_sum_to_zero(nums)
    assert not get_all_threes_that_sum_to_zero(nums)


def test_sum5():
    nums = [1, 50, 1, 25, -2, 10, 100, -10, 0]
    assert get_three_that_sum_to_zero(nums) == [1, 1, -2]
    assert get_all_threes_that_sum_to_zero(nums) == [(1, 1, -2), (10, -10, 0)]
