from InterviewCake.linked_list import *


# Works if cycles back to front or to middle of linked list
# O(n) time and O(n) space
def contains_cycle(node: LinkedListNode):
    nodes_seen = set()

    while node:
        if node.value in nodes_seen:
            return True
        nodes_seen.add(node.value)
        node = node.next

    return False
