from InterviewCake.linked_list_delete_node import *


def test_delete0():
    a = LinkedListNode('A')
    ll = LinkedList(None)
    ll.delete_node(a)
    assert not ll.root


def test_delete1():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    ll = LinkedList(a)
    ll.delete_node(b)
    assert a.next == c


def test_delete2():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    ll = LinkedList(a)
    ll.delete_node(a)
    assert ll.root == b
