from InterviewQuestions.digits_sum import *


def test_digits1():
    num = 99996
    target = 42
    assert do_digits_sum_to_target(num, target)


def test_digits2():
    num = 99996
    target = 43
    assert not do_digits_sum_to_target(num, target)


def test_digits3():
    num = 4200
    target = 6
    assert do_digits_sum_to_target(num, target)
