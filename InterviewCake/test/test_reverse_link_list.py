from InterviewCake.reverse_link_list import *
import pytest


def test_reverse1():
    n1 = LinkedListNode(1)
    n2 = LinkedListNode(2)
    n3 = LinkedListNode(3)
    n1.next = n2
    n2.next = n3

    r1 = LinkedListNode(1)
    r2 = LinkedListNode(2)
    r3 = LinkedListNode(3)
    r3.next = r2
    r2.next = r1

    assert reverse_link_list(n1) == r3


def test_two_elements():
    n1 = LinkedListNode(1)
    n2 = LinkedListNode(2)
    n1.next = n2

    r1 = LinkedListNode(1)
    r2 = LinkedListNode(2)
    r2.next = r1

    assert reverse_link_list(n1) == r2


def test_one_element():
    n1 = LinkedListNode(1)
    r1 = LinkedListNode(1)

    assert reverse_link_list(n1) == r1


def test_no_elements():
    assert reverse_link_list(None) is None
