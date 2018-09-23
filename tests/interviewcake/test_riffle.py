from interviewcake.riffle import *
import pytest


def test_riffle0():
    half1 = []
    half2 = []
    shuffled_deck = []
    assert is_single_riffle(shuffled_deck, half1, half2)


def test_riffle1():
    half1 = list(range(1, 26+1))
    half2 = list(range(27, 52+1))
    shuffled_deck = half1 + half2
    assert is_single_riffle(shuffled_deck, half1, half2)


def test_riffle2():
    half1 = [1, 2, 3]
    half2 = [4, 5, 6]
    shuffled_deck = [1, 4, 2, 5, 3, 6]
    assert is_single_riffle(shuffled_deck, half1, half2)


def test_riffle3():
    half1 = [1, 2, 3]
    half2 = [4, 5, 6, 7]
    shuffled_deck = [1, 2, 4, 5, 3, 6, 7]
    assert is_single_riffle(shuffled_deck, half1, half2)


def test_riffle4():
    half1 = [1, 2, 3]
    half2 = [4, 5, 6]
    shuffled_deck = [5, 1, 2, 4, 3, 6]
    assert not is_single_riffle(shuffled_deck, half1, half2)


def test_riffle5():
    half1 = [1, 2, 3]
    half2 = []
    shuffled_deck = [3, 1, 2]
    assert not is_single_riffle(shuffled_deck, half1, half2)


def test_riffle6():
    half1 = [1, 2, 3]
    half2 = []
    shuffled_deck = [1, 2, 3]
    assert is_single_riffle(shuffled_deck, half1, half2)


def test_riffle7():
    half1 = []
    half2 = [1, 2, 3]
    shuffled_deck = [1, 2]
    with pytest.raises(IndexError):
        is_single_riffle(shuffled_deck, half1, half2)


def test_riffle8():
    half1 = [1, 2, 1, 3]
    half2 = [4, 5, 6, 5, 4]
    shuffled_deck = [1, 4, 2, 1, 5, 6, 5, 3, 4]
    assert is_single_riffle(shuffled_deck, half1, half2)
