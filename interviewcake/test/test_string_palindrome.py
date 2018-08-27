from interviewcake.string_palindrome import *


def test_palindrome_yes():
    assert has_palindrome("civic")
    assert has_palindrome("ivicc")
    assert has_palindrome("a")
    assert has_palindrome("anna")
    assert has_palindrome("nana")


def test_palindrome_no():
    assert not has_palindrome("civil")
    assert not has_palindrome("livci")
    assert not has_palindrome("anka")
