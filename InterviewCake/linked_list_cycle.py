from InterviewCake.linked_list import *


# Works if cycles back to front or to middle of linked list
# Optimal solution is to use two runners of different speeds
# O(n) time and O(1) space
def contains_cycle(node: LinkedListNode):
    if not node:
        return False

    slow = fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
