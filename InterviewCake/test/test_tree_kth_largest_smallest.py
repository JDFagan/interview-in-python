from InterviewCake.tree_kth_largest_smallest import *


def test_no_elements():
    assert second_largest(None) is None
    assert kth_largest(1, None) is None
    assert kth_largest(2, None) is None
    assert kth_largest(3, None) is None
    assert kth_smallest(1, None) is None
    assert kth_smallest(2, None) is None
    assert kth_smallest(3, None) is None


def test_one_element():
    a = BinaryTreeNode(1)
    assert second_largest(a) is None
    assert kth_largest(1, a) == a
    assert kth_largest(2, a) is None
    assert kth_largest(3, a) is None
    assert kth_smallest(1, a) == a
    assert kth_smallest(2, a) is None
    assert kth_smallest(3, a) is None


def test_two_elements():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.right = b
    assert second_largest(a) == a
    assert kth_largest(1, a) == b
    assert kth_largest(2, a) == a
    assert kth_largest(3, a) is None
    assert kth_smallest(1, a) == a
    assert kth_smallest(2, a) == b
    assert kth_smallest(3, a) is None


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
    assert kth_largest(1, a) == e
    assert kth_largest(2, a) == d
    assert kth_largest(3, a) == c
    assert kth_smallest(1, a) == a
    assert kth_smallest(2, a) == b
    assert kth_smallest(3, a) == c


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
    assert kth_largest(1, a) == a
    assert kth_largest(2, a) == b
    assert kth_largest(3, a) == c
    assert kth_smallest(1, a) == e
    assert kth_smallest(2, a) == d
    assert kth_smallest(3, a) == c


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
    assert kth_largest(1, a) == e
    assert kth_largest(2, a) == b
    assert kth_largest(3, a) == a
    assert kth_smallest(1, a) == d
    assert kth_smallest(2, a) == c
    assert kth_smallest(3, a) == a


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
    assert kth_largest(1, a) == a
    assert kth_largest(2, a) == e
    assert kth_largest(3, a) == c
    assert kth_smallest(1, a) == b
    assert kth_smallest(2, a) == d
    assert kth_smallest(3, a) == c
