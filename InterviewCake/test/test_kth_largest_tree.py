from InterviewCake.kth_largest_tree import *


def test_no_elements():
    assert get_kth_largest(2, None) is None


def test_one_element():
    a = BinaryTreeNode(1)
    assert get_kth_largest(2, a) is None


def test_k_elements():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.right = b
    assert get_kth_largest(2, a) == a
