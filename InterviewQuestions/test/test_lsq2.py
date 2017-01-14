from InterviewQuestions.lsq2 import *


def test_lsq1():
    parseThis = '{"foo":"bar"}'
    assert json_parser(parseThis) == {'foo':'bar'}
