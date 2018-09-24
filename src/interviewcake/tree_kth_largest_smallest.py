from interviewcake.tree_binary import *


def largest(node: BinaryTreeNode):
    while node.right:
        node = node.right
    return node


def second_largest(node: BinaryTreeNode):
    prev_largest = None
    while node:
        if node.right:
            prev_largest = node
            node = node.right
            continue

        if node.left:
            return largest(node.left)
        else:
            break

    return prev_largest


def kth_largest(k, node: BinaryTreeNode):
    if node is None:
        return None

    stack = []
    while node or len(stack) != 0:
        if node:
            stack.append(node)
            node = node.right
        else:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node
            node = node.left

    return node


def kth_smallest(k, node: BinaryTreeNode):
    if node is None:
        return None

    stack = []
    while node or len(stack) != 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node
            node = node.right

    return node
