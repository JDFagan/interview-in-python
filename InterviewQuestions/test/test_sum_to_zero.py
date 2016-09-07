from InterviewQuestions.sum_to_zero import *


def test_sum0():
    nums = []
    assert not get_three_that_sum_to_zero(nums)


def test_sum1():
    nums = [1, 1, -2]
    assert get_three_that_sum_to_zero(nums) == [1, 1, -2]


def test_sum2():
    nums = [1, 50, 1, 25, -2]
    assert get_three_that_sum_to_zero(nums) == [1, 1, -2]


def test_sum3():
    nums = [12, 50, 1, 25, -2]
    assert get_three_that_sum_to_zero(nums) is None


def test_sum3():
    nums = [1, 50, 1, 25, -2, 10, 100, -10, 0]
    assert get_three_that_sum_to_zero(nums) == [10, -10, 0]
