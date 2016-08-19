class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


def reverse_link_list(head: LinkedListNode):
    prev = None

    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

#
# def reverse_link_list2(head: LinkedListNode):
#     if head is None:
#         return head
#
#     next = head.next
#
#     prev = head
#     next = reverse_link_list(head.next)
#     if head is None:
#         head = prev
#     else:
#         head.next = prev
#
#     return head