from interviewcake.okeros import *


def test_okeros1():
    r1 = {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}
    r2 = {'bottom_y': 6, 'height': 10, 'left_x': 8, 'width': 4}
    assert get_rectangular_intersection(r1, r2) == {'bottom_y': 6, 'height': 3, 'left_x': 8, 'width': 3}


def test_okeros_no_intersection():
    r1 = {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}
    r2 = {'bottom_y': 60, 'height': 10, 'left_x': 80, 'width': 4}
    assert get_rectangular_intersection(r1, r2) is None


def test_okeros_within():
    r1 = {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}
    r2 = {'bottom_y': 4, 'height': 10, 'left_x': 0, 'width': 14}
    assert get_rectangular_intersection(r1, r2) == {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}


def test_okeros_share_edge():
    r1 = {'bottom_y': 5, 'height': 4, 'left_x': 1, 'width': 10}
    r2 = {'bottom_y': 9, 'height': 10, 'left_x': 0, 'width': 14}
    assert get_rectangular_intersection(r1, r2) == {'bottom_y': 9, 'height': 0, 'left_x': 1, 'width': 10}


