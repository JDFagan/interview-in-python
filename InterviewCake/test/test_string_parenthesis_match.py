from InterviewCake.string_parenthesis_match import *
import pytest


def test_parens_error1():
    input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"
    with pytest.raises(IndexError):
        match(input, -10)


def test_parens_error2():
    input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"
    with pytest.raises(IndexError):
        match(input, 1000)


def test_parens_error3():
    input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"
    with pytest.raises(IndexError):
        match(input, 5)


def test_parens1():
    input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing"
    assert match(input, 10) == 79


def test_parens2():
    input = "()"
    assert match(input, 0) == 1


def test_parens3():
    input = "(a)"
    assert match(input, 0) == 2


def test_parens4():
    input = "(a(b))"
    assert match(input, 0) == 5


def test_parens5():
    input = "(a(b)"
    assert match(input, 0) is None
