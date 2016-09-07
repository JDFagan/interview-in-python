from InterviewCake.linked_list import *


# O(n) time and O(1) space
def contains_cycle(node: LinkedListNode):
    result = False
    starting_node = node

    while node:
        if not node.next:
            break
        if node.next == starting_node:
            result = True
            break
        node = node.next

    return result
