from interviewcake.linked_list_cycle import *


def test_cycle_empty():
    a = None

    assert not contains_cycle(a)


def test_cycle_one_element_has_cycle():
    a = LinkedListNode("Angel Food")

    assert not contains_cycle(a)


def test_cycle_one_element_no_cycle():
    a = LinkedListNode("Angel Food")

    a.next = a

    assert contains_cycle(a)


def test_cycle0():
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    assert not contains_cycle(a)


def test_cycle1():
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = a

    assert contains_cycle(a)


def test_cycle2():
    a = LinkedListNode("Angel Food")
    b = LinkedListNode("Bundt")
    c = LinkedListNode("Cheese")
    d = LinkedListNode("Devil's Food")
    e = LinkedListNode("Eccles")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c

    assert contains_cycle(a)
