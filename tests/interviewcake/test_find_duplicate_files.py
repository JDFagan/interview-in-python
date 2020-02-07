import os

from interviewcake.find_duplicate_files import find_duplicate_files

test_dir = '~/Repositories/JDFagan/interview-in-python/src/questions/duplicate_file_test'


def test_find_dup1():
    expected = []
    assert expected == find_duplicate_files(starting_dir=os.path.expanduser(f'{test_dir}/empty_dir/'))


def test_find_dup2():
    expected = []
    expected.append((os.path.expanduser(f'{test_dir}/sub1/__init__.py'), os.path.expanduser(f'{test_dir}/sub1/empty')))
    assert expected == find_duplicate_files(starting_dir=os.path.expanduser(f'{test_dir}/sub1/'))


def test_find_dup3():
    expected = []
    assert expected == find_duplicate_files(starting_dir=os.path.expanduser(test_dir))
