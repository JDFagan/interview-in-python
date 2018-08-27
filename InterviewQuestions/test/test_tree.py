from InterviewQuestions import tree


def test1():
    """
           3
          /| \
         1 4 11
        / / \ \
       0  2 5  3
    :return: [3, 16, 10]
    """
    # Build the tree
    r = tree.TreeNode(3)

    n = tree.TreeNode(1)
    n.insert(tree.TreeNode(0))
    r.insert(n)

    n = tree.TreeNode(4)
    n.insert(tree.TreeNode(2))
    n.insert(tree.TreeNode(5))
    r.insert(n)

    n = tree.TreeNode(11)
    n.insert(tree.TreeNode(3))
    r.insert(n)

    t = tree.Tree(root=r)
    assert t.sum_levels() == [3, 16, 10]
