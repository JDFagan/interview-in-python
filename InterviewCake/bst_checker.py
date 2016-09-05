from InterviewCake.binary_tree import *


def largest(node):
    while node.right:
        node = node.right
    return node


# O(n) time and O(h) space where h is height of tree
def is_binary_search_tree(node):
    if node is None:
        return True
    if node.left is None:
        if node.right is None:
            return True
        return node.value < node.right.value and node.value < largest(node.right).value \
                and is_binary_search_tree(node.right)
    elif node.right is None:
        return node.value > node.left.value and node.value > largest(node.left).value \
                and is_binary_search_tree(node.left)

    return node.left.value < node.value < node.right.value \
            and largest(node.left).value < node.value < largest(node.right).value \
            and is_binary_search_tree(node.left) and is_binary_search_tree(node.right)
