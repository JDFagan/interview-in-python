from interviewcake.tree_binary import *


def largest(node: BinaryTreeNode):
    while node.right:
        node = node.right
    return node


# Use depth-first search testing for validity for each node as we go
# O(n) time and O(h) space where h is height of tree
def is_binary_search_tree(node: BinaryTreeNode):
    if not node:
        return True
    if not node.left:
        if not node.right:
            return True
        return node.value < node.right.value and node.value < largest(node.right).value \
                and is_binary_search_tree(node.right)
    elif not node.right:
        return node.value > node.left.value and node.value > largest(node.left).value \
                and is_binary_search_tree(node.left)

    return node.left.value < node.value < node.right.value \
            and largest(node.left).value < node.value < largest(node.right).value \
            and is_binary_search_tree(node.left) and is_binary_search_tree(node.right)
