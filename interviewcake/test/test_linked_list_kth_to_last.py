from interviewcake.linked_list import *
from interviewcake.linked_list_kth_to_last import *

def test_kth_linked_list1():
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert kth_to_last_node(2, a) == d

def test_no_elements():
    assert kth_to_last_node(2, None) == None

def test_short_list():
    a = LinkedListNode("Angel Food")

    assert kth_to_last_node(2, a) == None

def test_exact_list():
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    a.next = b

    assert kth_to_last_node(2, a) == a
