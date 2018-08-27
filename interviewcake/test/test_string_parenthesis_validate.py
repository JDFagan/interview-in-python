from interviewcake.string_parenthesis_validate import *


def test_validate0():
    code = ""
    assert braces_brackets_parentheses_validate(code)


def test_validate1():
    code = "{ [ ] ( ) }"
    assert braces_brackets_parentheses_validate(code)


def test_validate2():
    code = "{ [ ( ] ) }"
    assert not braces_brackets_parentheses_validate(code)


def test_validate3():
    code = "{ [ }"
    assert not braces_brackets_parentheses_validate(code)
