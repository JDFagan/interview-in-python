from InterviewCake.binary_tree import *


def largest(node):
    if node.right:
        return largest(node.right)
    return node


def second_largest(node):
    if node is None or (node.right is None and node.left is None):
        return None

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


def get_kth_largest(k, node):
    biggest = []
    nodes = [None]

    # Edge cases
    if node is None:
        return None
    if k >= 2 and node.right is None and node.left is None:
        return None
    if k <= 0:
        raise IndexError("Impossible to find kth largest if 0 or negative k")

    while k > 1:
        current = node

    # Iterative approach fails..
    # biggest = [3]
    # nodes = [None, 1]
    # node = 2
    # 1 - 2 - 3
    # Fly down right side of tree to start appending largest values
    while node:
        if node.right is None:
            if node.left is None:
                biggest.append(node)
                node = nodes.pop()
            else:
                nodes.append(node)
                node = node.left
        else:
            nodes.append(node)
            node = node.right

    if len(biggest) < k:
        return None

    return biggest[k - 1]
