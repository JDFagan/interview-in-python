from interviewcake.hical import *
import pytest


def test_hical1():
    meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    assert condense_meeting_times(meetings=meetings) == [(0, 1), (3, 8), (9, 12)]


def test_hical2():
    meetings = [(0, 1), (3, 5), (7, 8), (10, 12), (9, 10), (4, 6)]
    assert condense_meeting_times(meetings=meetings) == [(0, 1), (3, 6), (7, 8), (9, 12)]


def test_hical3():
    meetings = [(1, 2), (2, 3)]
    assert condense_meeting_times(meetings=meetings) == [(1, 3)]


def test_hical4():
    meetings = [(1, 5), (2, 3)]
    assert condense_meeting_times(meetings=meetings) == [(1, 5)]


def test_hical5():
    meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
    assert condense_meeting_times(meetings=meetings) == [(1, 10)]


def test_three_meetings():
    meetings = [(1, 2), (5, 8), (0, 9)]
    assert condense_meeting_times(meetings=meetings) == [(0, 9)]


def test_two_meetings():
    meetings = [(0, 2), (5, 8)]
    assert condense_meeting_times(meetings=meetings) == [(0, 2), (5, 8)]


def test_one_meetings():
    meetings = [(0, 2)]
    assert condense_meeting_times(meetings=meetings) == [(0, 2)]


def test_no_meetings():
    meetings = []
    assert condense_meeting_times(meetings=meetings) == []
