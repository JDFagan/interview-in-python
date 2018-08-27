from questions.regex import *


def test_regex1():
    assert match('abc', 'abc')


def test_regex2():
    assert match('abc', 'a.c')


def test_regex3():
    assert match('abcccc', 'a.c*')


def test_regex4():
    assert not match('abccccd', 'a.c*')


def test_regex4():
    assert match('abccccd', 'a.c*d')
