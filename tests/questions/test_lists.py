from questions.lists import *


def test_bad_list_type():
    ints = ['a', 'b']
    target = 0
    expected_result = False
    assert expected_result == adds_up_to_this_int(ints=ints, target=target)


def test_empty_list_bad_target():
    ints = []
    target = 0
    expected_result = False
    assert expected_result == adds_up_to_this_int(ints=ints, target=target)


def test_empty_list_good_target():
    ints = []
    target = None
    expected_result = True
    assert expected_result == adds_up_to_this_int(ints=ints, target=target)
