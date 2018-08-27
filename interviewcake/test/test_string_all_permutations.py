from interviewcake.string_all_permutations import *


def test_permutations1():
    string = "a"
    assert get_permutations(string) == set(["a"])


def test_permutations2():
    string = "ab"
    assert get_permutations(string) == set(["ab", "ba"])


def test_permutations3():
    string = "cat"
    assert get_permutations(string) == set(["cat", "cta", "atc", "act", "tac", "tca"])
