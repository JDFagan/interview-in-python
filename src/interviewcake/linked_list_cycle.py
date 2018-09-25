from interviewcake.linked_list import *


# Works if cycles back to front or to middle of linked list
# Optimal solution is to use two runners of different speeds
# O(n) time and O(1) space
def contains_cycle(node: LinkedListNode):
    if not node:
        return False

    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            # we have cycled around and caught up to the slow runner
            return True

    return False
