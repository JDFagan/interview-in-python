from InterviewCake.tree_binary import *


# Recursive depth first implementation
def get_depth(node: BinaryTreeNode, aggregate):
    if node is None:
        return 0

    if node.left is None and node.right is None:            # leaf
        return 1
    elif node.left is not None and node.right is None:      # right leaf
        return aggregate(get_depth(node.left, aggregate), 0) + 1
    elif node.left is None and node.right is not None:      # left leaf
        return aggregate(0, get_depth(node.right, aggregate)) + 1
    else:
        return aggregate(get_depth(node.left, aggregate), get_depth(node.right, aggregate)) + 1


# O(2n) time and O(n) space (due to recursive stack)
def is_super_balanced(node: BinaryTreeNode):
    return get_depth(node, max) - get_depth(node, min) <= 1
