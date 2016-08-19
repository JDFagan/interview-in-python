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


# O(n) time and O(1) space
def reverse_link_list(head: LinkedListNode):
    prev = None

    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev
