from InterviewCake.stack import *


def test_no_elements():
    s = MaxStack()
    assert not s.get_max()


def test_stack1():
    s = MaxStack()
    s.push(1)
    s.push(30)
    s.push(-10)
    s.push(0)
    assert s.get_max() == 30
    s.push(34)
    assert s.get_max() == 34
    assert s.pop() == 34
    assert s.pop() == 0
    assert s.pop() == -10
    assert s.pop() == 30
    assert s.get_max() == 1
    assert s.pop() == 1
    assert not s.get_max()
    assert not s.pop()
    assert not s.pop()
