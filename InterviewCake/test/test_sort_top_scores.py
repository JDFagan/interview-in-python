from InterviewCake.sort import *


def test_sort0():
    unsorted_scores = []
    HIGHEST_POSSIBLE_SCORE = 100
    assert counting_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE) == []


def test_sort1():
    unsorted_scores = [37, 89, 41, 65, 91, 53]
    HIGHEST_POSSIBLE_SCORE = 100
    assert counting_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE) == [37, 41, 53, 65, 89, 91]
