from InterviewCake.fibonacci import *
import pytest


def test_fib_error():
    n = -1
    with pytest.raises(IndexError):
        fib(n)


def test_fib0():
    n = 0
    assert fib(n) == 0


def test_fib1():
    n = 1
    assert fib(n) == 1


def test_fib2():
    n = 2
    assert fib(n) == 1


def test_fib3():
    n = 3
    assert fib(n) == 2


def test_fib4():
    n = 4
    assert fib(n) == 3


def test_fib5():
    n = 5
    assert fib(n) == 5


def test_fib6():
    n = 6
    assert fib(n) == 8


def test_fib7():
    n = 7
    assert fib(n) == 13
