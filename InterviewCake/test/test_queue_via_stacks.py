from InterviewCake.queue_via_stacks import *
import pytest


def test_queue1():
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

    q.enqueue(4)
    q.enqueue(5)
    assert q.as_list() == [3, 4, 5]
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5
    with pytest.raises(IndexError):
        assert q.dequeue()
