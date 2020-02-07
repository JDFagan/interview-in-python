import os
import glob

import hashlib


def find_duplicate_files(starting_dir: str=os.path.abspath(os.curdir)):
    """
    Strategy: dups will definitely have same file size and should have same hash of its contents
        files[hash] = ('/path/to/file', created_date)

    O(n) time and O(n + d) space (where n in input files and d is number of duplicate files).

    :param starting_dir: path as string
    :return: list of tuples where each tuple represents pair of duplicate files
    """
    files = {}
    duplicate_files = []

    # for filename in glob.glob(starting_dir, recursive=True):
    return duplicate_files
