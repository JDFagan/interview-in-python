from InterviewCake.merge_lists import *


def test_no_elements():
    list1 = []
    list2 = []
    assert merge_lists(list1, list2) == []

def test_no_elements1():
    list1 = []
    list2 = [1, 2]
    assert merge_lists(list1, list2) == [1, 2]


def test_no_elements2():
    list1 = [1, 9]
    list2 = []
    assert merge_lists(list1, list2) == [1, 9]


def test_merge1():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert merge_lists(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_merge2():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    assert merge_lists(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_merge3():
    list1 = [-3, 5, 20]
    list2 = [2, 4, 6, 10]
    assert merge_lists(list1, list2) == [-3, 2, 4, 5, 6, 10, 20]


def test_merge4():
    list1 = [1, 2, 3]
    list2 = [3, 5, 6]
    assert merge_lists(list1, list2) == [1, 2, 3, 3, 5, 6]


def test_merge5():
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]
    assert merge_lists(my_list, alices_list) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
