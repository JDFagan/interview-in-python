from InterviewCake.linked_list import *


# O(1) time and O(1) space!
class LinkedList:
    def __init__(self, root: LinkedListNode):
        self.root = root

    def delete_node(self, node: LinkedListNode):
        if node.next:
            node.value = node.next.value
            node.next = node.next.next
        else:
            node = node.next
