from InterviewCake.stolen_breakfast_drone import *


def test_no_elements():
    delivery_ids = []
    assert find_missing_drones(delivery_ids) == set([])


def test_drone1():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 5]
    assert find_missing_drones(delivery_ids) == set([2])


def test_drone2():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 3, 5]
    assert find_missing_drones(delivery_ids) == set([2, 3])


def test_no_missing():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 5, 2]
    assert find_missing_drones(delivery_ids) == set([])


def test_no_elements2():
    delivery_ids = []
    assert find_missing_drone(delivery_ids) == 0


def test_drone12():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 5]
    assert find_missing_drone(delivery_ids) == 2


def test_drone22():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 3, 5]
    assert find_missing_drone(delivery_ids) == 1


def test_no_missing2():
    delivery_ids = [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 5, 2]
    assert find_missing_drone(delivery_ids) == 0
