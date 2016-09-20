from InterviewCake.find_repeating_num import *


def test_no_elements():
    nums = []
    assert find_repeating_num_in_range(nums) is None


def test_one_element():
    nums = [1]
    assert find_repeating_num_in_range(nums) is None


def test_repeating0():
    nums = [1, 2, 3]
    assert find_repeating_num_in_range(nums) is None


def test_repeating1():
    nums = [1, 2, 2, 3]
    assert find_repeating_num_in_range(nums) == 2


def test_repeating2():
    nums = [1, 2, 2, 2, 3]
    assert find_repeating_num_in_range(nums) == 2


def test_repeating3():
    nums = [1, 2, 2, 3, 4]
    assert find_repeating_num_in_range(nums) == 2


def test_repeating4():
    nums = [1, 2, 2, 2, 3, 4]
    assert find_repeating_num_in_range(nums) == 2


def test_repeating5():
    nums = [1, 2, 2, 2, 3, 4, 4]
    assert find_repeating_num_in_range(nums) == 2


def test_repeating6():
    nums = [1, 2, 3, 4, 4]
    assert find_repeating_num_in_range(nums) == 4


def test_repeating7():
    nums = [1, 1, 2, 3, 4, 5, 6, 7]
    assert find_repeating_num_in_range(nums) == 1


def test_repeating8():
    nums = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
    assert find_repeating_num_in_range(nums) == 3


def test_repeating9():
    nums = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_repeating_num_in_range(nums) == 3


def test_repeating10():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert find_repeating_num_in_range(nums) is None


def test_repeating11():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert find_repeating_num_in_range(nums) == 11
