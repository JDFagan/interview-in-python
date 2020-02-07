import os

from interviewcake.find_duplicate_files import find_duplicate_files


def test_find_dup1():
    dir = os.path.expanduser("~/Repositories/JDFagan/interview-in-python/tests/interviewcake/")
    expected = []
    assert expected == find_duplicate_files(starting_dir=dir)


def test_find_dup2():
    dir = os.path.expanduser("~/Repositories/JDFagan/interview-in-python/src/interviewcake/")
    expected = []
    # expected = [('/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/__init__.py',
    #             '/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/trollolol/__init__.py')]
    expected.append(('/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/__init__.py',
                     '/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/trollolol/__init__.py'))
    expected.append(('/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/problem.txt',
                     '/Users/jdfagan/Repositories/JDFagan/interview-in-python/src/interviewcake/trollolol/haha.py'))
    assert expected == find_duplicate_files(starting_dir=dir)


def test_find_dup3():
    dir = os.path.expanduser("/Users/JDFagan/Repositories/JDFagan/interview-in-python/src/interviewcake/empty/")
    expected = []
    assert expected == find_duplicate_files(starting_dir=dir)
