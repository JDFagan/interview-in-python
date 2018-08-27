from interviewcake.rotation_point import *


def test_no_elements():
    words = []
    assert find_rotation_point(words) == -1


def test_one_element():
    words = [
        'ptolemaic',
    ]
    assert find_rotation_point(words) == -1


def test_two_elements():
    words = [
        'xenoepist',
        'asymptote',  # <-- rotates here!
    ]
    assert find_rotation_point(words) == 1


def test_two_elements2():
    words = [
        'asymptote',  # <-- rotates here!
        'xenoepist',
    ]
    assert find_rotation_point(words) == 0


def test_search1():
    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',  # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]
    assert find_rotation_point(words) == 5


def test_search2():
    words = [
        'othellolagkage',
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',  # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
    ]
    assert find_rotation_point(words) == 6


def test_search3():
    words = [
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',  # <-- rotates here!
    ]
    assert find_rotation_point(words) == 10


def test_search4():
    words = [
        'asymptote',  # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
    ]
    assert find_rotation_point(words) == 0
