from InterviewQuestions.regex import *


def test_regex1():
    assert match('abc', 'abc')


def test_regex2():
    assert match('abc', 'a.c')


def test_regex3():
    assert match('abcccc', 'a.c*')
