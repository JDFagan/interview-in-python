from InterviewCake.fibonacci import *
import pytest


def test_fib_memoization():
    fibber = Fibonacci()
    assert fibber.fib(8) == 21
    with pytest.raises(IndexError):
        assert fibber.fib(-1)
    assert fibber.fib(0) == 0
    assert fibber.fib(1) == 1
    assert fibber.fib(2) == 1
    assert fibber.fib(3) == 2
    assert fibber.fib(4) == 3
    assert fibber.fib(5) == 5
    assert fibber.fib(6) == 8
    assert fibber.fib(7) == 13


def test_fib_error():
    n = -1
    with pytest.raises(IndexError):
        fib_recursive(n)


def test_fib0():
    n = 0
    assert fib_recursive(n) == 0


def test_fib1():
    n = 1
    assert fib_recursive(n) == 1


def test_fib2():
    n = 2
    assert fib_recursive(n) == 1


def test_fib3():
    n = 3
    assert fib_recursive(n) == 2


def test_fib4():
    n = 4
    assert fib_recursive(n) == 3


def test_fib5():
    n = 5
    assert fib_recursive(n) == 5


def test_fib6():
    n = 6
    assert fib_recursive(n) == 8


def test_fib7():
    n = 7
    assert fib_recursive(n) == 13
