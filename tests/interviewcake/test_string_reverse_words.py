from interviewcake.string_reverse_words import *


def test_reverse_words_none():
    words = None
    assert reverse_words(words) == None


def test_reverse_words0():
    words = ""
    assert reverse_words(words) == ""


def test_reverse_words1():
    words = "Hello"
    assert reverse_words(words) == "Hello"


def test_reverse_words2():
    words = "Hello World"
    assert reverse_words(words) == "World Hello"


def test_reverse_words3():
    words = "abc def"
    assert reverse_words(words) == "def abc"


def test_reverse_words4():
    words = "find you will pain only go you recordings security the into if"
    assert reverse_words(words) == "if into the security recordings you go only pain will you find"
