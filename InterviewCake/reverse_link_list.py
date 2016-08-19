from InterviewCake.linked_list import *
from copy import deepcopy


# O(n) time and O(1) space
def reverse_link_list(head: LinkedListNode):
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


def reverse_link_list_out_of_place(head: LinkedListNode):
    current = deepcopy(head)
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev
