from interviewcake.tree_super_balanced import *


def test_super_balanced_tree1():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    a.left = b
    a.right = c
    assert is_super_balanced(a)


def test_super_balanced_tree2():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    assert is_super_balanced(a)


def test_super_balanced_tree3():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    assert is_super_balanced(a)


def test_super_balanced_tree4():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    f = BinaryTreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    d.right = f
    assert not is_super_balanced(a)


def test_list():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    a.right = b
    b.right = c
    assert not is_super_balanced(a)


def test_left_leaf():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.right = b
    assert is_super_balanced(a)


def test_right_leaf():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.left = b
    assert is_super_balanced(a)


def test_one_elements():
    a = BinaryTreeNode(1)
    assert is_super_balanced(a)


def test_no_elements():
    assert is_super_balanced(None)
