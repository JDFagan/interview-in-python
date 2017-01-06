from InterviewQuestions.lsq import *


def test_lsq1():
    digits = [2, 2]
    words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}

    assert t9(digits, words) == {'cat', 'cab', 'cats', 'aardvark', 'abacus'}
