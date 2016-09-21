from InterviewCake.find_duplicate_files import *
from os.path import expanduser


def test_find_dup1():
    dir = expanduser("~/Repositories/JDFagan/InterviewInPython/InterviewCake/test")
    expected = []
    assert find_duplicate_files(starting_dir=dir) == expected


def test_find_dup2():
    dir = expanduser("~/Repositories/JDFagan/InterviewInPython/InterviewCake/")
    expected = []
    expected.append(('/Users/JDFagan/Repositories/JDFagan/InterviewInPython/InterviewCake/__init__.py',
                     '/Users/JDFagan/Repositories/JDFagan/InterviewInPython/InterviewCake/test/__init__.py'))
    expected.append(('/Users/JDFagan/Repositories/JDFagan/InterviewInPython/InterviewCake/problem.txt',
                     '/Users/JDFagan/Repositories/JDFagan/InterviewInPython/InterviewCake/trollolol/haha.py'))
    assert find_duplicate_files(starting_dir=dir) == expected
