from InterviewCake.binary_tree import *

def get_kth_largest(k, node):
    biggest = []
    nodes = [None]

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
