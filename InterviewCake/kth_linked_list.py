from InterviewCake.linked_list import *
from copy import deepcopy

# O(2n) time and O(1) space
def kth_to_last_node(k, node: LinkedListNode):
    result = None
    prev = None

    # Build the prev linked list
    while node:
        node_next = node.next
        if prev is None:
            prev = node
            prev.next = None
        else:
            next = prev
            prev = node
            prev.next = next
        node = node_next

    # Now find the kth last node
    i = 1
    while i <= k and prev:
        if i == k:
            result = prev
        prev = prev.next
        i += 1

    return result
