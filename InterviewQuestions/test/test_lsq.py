from InterviewQuestions.lsq import *


def test_lsq1():
    digits = [2, 2]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'zoo', 'hat'}
    assert t9(digits, words) == {'cat', 'cab', 'cats', 'aardvark', 'abacus'}


def test_lsq2():
    digits = [2, 2]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == {'cat', 'cab', 'cats', 'aardvark', 'abacus'}


def test_lsq3():
    digits = [2, 3]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == {'ads'}


def test_lsq4():
    digits = [0]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == set()


def test_lsq5():
    digits = [1, 1]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == set()


def test_lsq6():
    digits = [3, 2]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == set()


def test_lsq7():
    digits = [9]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
    assert t9(digits, words) == {'zoo'}
