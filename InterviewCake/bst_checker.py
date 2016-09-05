from InterviewCake.binary_tree import *


# O(n) time and O(h) space where h is height of tree
def is_binary_search_tree(node):
    if node is None:
        return True
    if node.left is None:
        if node.right is None:
            return True
        return node.value < node.right.value and is_binary_search_tree(node.right)
    elif node.right is None:
        return node.value > node.left.value and is_binary_search_tree(node.left)

    return node.left.value < node.value < node.right.value \
            and is_binary_search_tree(node.left) and is_binary_search_tree(node.right)
