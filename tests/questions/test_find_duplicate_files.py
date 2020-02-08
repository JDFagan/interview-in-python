import os

from questions.find_duplicate_files import find_duplicate_files

test_dir = os.path.expanduser('~/Repositories/JDFagan/interview-in-python/src/questions/duplicate_file_test')


def test_find_dup1():
    dir = f'{test_dir}/empty_dir/'
    expected = {}
    assert find_duplicate_files(starting_dir=dir) == expected


def test_find_dup2():
    dir = f'{test_dir}/sub1/'
    expected = {
        0: {'__init__.py', 'empty'},
        }
    assert find_duplicate_files(starting_dir=dir) == expected


def test_find_dup3():
    dir = test_dir
    expected = {
        0: {'__init__.py', 'sub1/__init__.py', 'sub1/empty'},
        13: {'ha.py', 'ha.txt', 'sub1/hehe.txt'},
        }
    assert find_duplicate_files(starting_dir=dir) == expected
