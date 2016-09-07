from InterviewCake.linked_list import *


# O(n) time and O(1) space
class LinkedList:
    def __init__(self, root: LinkedListNode):
        self.root = root

    def delete_node(self, node: LinkedListNode):
        prev = current = self.root

        while current:
            if current == node:
                if prev == self.root:       # edge root case
                    self.root = node.next
                prev.next = node.next
                break
            else:
                prev = current
                current = current.next
