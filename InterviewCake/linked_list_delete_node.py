from InterviewCake.linked_list import *


# O(1) time and O(1) space!
# Note, this solution is risky instead of walking from root to where we need to delete.  The reason why
# is because we are editing the linked list in place and leaving some dangling nodes.  If there are other
# pointers to these nodes that got left off due to this algorithm, it could incur subtle side effect bugs!
class LinkedList:
    def __init__(self, root: LinkedListNode):
        self.root = root

    def delete_node(self, node: LinkedListNode):
        if node.next:
            node.value = node.next.value
            node.next = node.next.next
        else:
            node = node.next
