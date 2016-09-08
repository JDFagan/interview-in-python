from InterviewCake.string_reverse import *


def test_reverse_string_none():
    s = None
    assert reverse_string(s) == None


def test_reverse_string0():
    s = ""
    assert reverse_string(s) == ""


def test_reverse_string1():
    s = "Hello World!"
    assert reverse_string(s) == "!dlroW olleH"


def test_reverse_string2():
    s = "Hello World"
    assert reverse_string(s) == "dlroW olleH"


def test_reverse_string3():
    s = "abc"
    assert reverse_string(s) == "cba"


def test_reverse_string4():
    s = "abcd"
    assert reverse_string(s) == "dcba"
