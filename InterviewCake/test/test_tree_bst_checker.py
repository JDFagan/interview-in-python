from InterviewCake.tree_bst_checker import *


def test_no_elements():
    assert is_binary_search_tree(None)


def test_one_element():
    a = BinaryTreeNode(1)
    assert is_binary_search_tree(a)


def test_bst_bad():
    a = BinaryTreeNode(50)
    b = BinaryTreeNode(30)
    c = BinaryTreeNode(20)
    d = BinaryTreeNode(60)
    e = BinaryTreeNode(80)
    f = BinaryTreeNode(70)
    g = BinaryTreeNode(90)
    a.left = b
    b.left = c
    b.right = d
    a.right = e
    e.left = f
    e.right = g
    assert not is_binary_search_tree(a)


def test_bst_good1():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.right = b
    assert is_binary_search_tree(a)


def test_bst_bad1():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    a.left = b
    assert not is_binary_search_tree(a)


def test_bst_good2():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    a.right = b
    b.right = c
    c.right = d
    d.right = e
    assert is_binary_search_tree(a)


def test_bst_bad2():
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    a.right = b
    b.right = c
    c.right = d
    d.left = e
    assert not is_binary_search_tree(a)


def test_bst_good3():
    a = BinaryTreeNode(5)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(2)
    e = BinaryTreeNode(1)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    assert is_binary_search_tree(a)


def test_bst_bad3():
    a = BinaryTreeNode(5)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(2)
    e = BinaryTreeNode(1)
    a.right = b
    b.left = c
    c.left = d
    d.left = e
    assert not is_binary_search_tree(a)


def test_bst_good4():
    a = BinaryTreeNode(3)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(2)
    d = BinaryTreeNode(1)
    e = BinaryTreeNode(5)
    a.right = b
    a.left = c
    c.left = d
    b.right = e
    assert is_binary_search_tree(a)


def test_bst_bad4():
    a = BinaryTreeNode(3)
    b = BinaryTreeNode(4)
    c = BinaryTreeNode(2)
    d = BinaryTreeNode(1)
    e = BinaryTreeNode(5)
    a.right = b
    a.left = c
    c.right = d
    b.right = e
    assert not is_binary_search_tree(a)


def test_bst_good5():
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

    assert is_binary_search_tree(a)


def test_bst_bad5():
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
    a.right = d
    d.right = b
    d.left = b.right
    b.left = b.right = None

    # adding 4
    c.left = e

    assert not is_binary_search_tree(a)
