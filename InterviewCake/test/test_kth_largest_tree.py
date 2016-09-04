from InterviewCake.kth_largest_tree import *


def test_no_elements():
    assert second_largest(None) is None


def test_one_element():
    a = BinaryTreeNode(1)
    assert second_largest(a) is None


def test_two_elements():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.right = b
    assert second_largest(a) == a


def test_right_elements():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    a.right = b
    b.right = c
    c.right = d
    d.right = e
    assert second_largest(a) == d


def test_left_elements():
    a = BinaryTreeNode(5)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(2)
    e = BinaryTreeNode(1)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    assert second_largest(a) == b


def test_tree1():
    a = BinaryTreeNode(3)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(2)
    d = BinaryTreeNode(1)
    e = BinaryTreeNode(5)
    a.right = b
    a.left = c
    c.left = d
    b.right = e
    assert second_largest(a) == b


def test_tree2():
    a = BinaryTreeNode(5)
    b = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(2)
    e = BinaryTreeNode(4)

    # adding 1
    a.left = b

    # adding 3
    b.right = c

    # adding 2
    a.left = d
    d.left = b
    d.right = b.right
    b.left = b.right = None

    # adding 4
    c.right = e

    assert second_largest(a) == e


# def test_no_elements():
#     assert get_kth_largest(2, None) is None
#
#
# def test_one_element():
#     a = BinaryTreeNode(1)
#     assert get_kth_largest(2, a) is None
#
#
# def test_k_elements():
#     a = BinaryTreeNode(1)
#     b = BinaryTreeNode(2)
#     a.right = b
#     assert get_kth_largest(2, a) == a
