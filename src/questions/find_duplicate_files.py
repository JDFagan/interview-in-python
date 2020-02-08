import os
import glob

import hashlib


def find_duplicate_files(starting_dir: str=os.path.abspath(os.curdir)):
    """
    Strategy: dups will definitely have same file size and should have same hash of its contents
        files[hash] = ('/path/to/file', created_date)

    O(n) time and O(n + d) space (where n in input files and d is number of duplicate files).

    :param starting_dir: path as string
    :return: set of duplicate file sets where each set represents a unique duplicate file shown with the collection of
    file paths
    """
    files = {}
    duplicate_files = []

    os.chdir(starting_dir)
    print(f"Finding dupe sets within {starting_dir}")
    for filename in glob.glob('**/*', recursive=True):
        hash = os.path.getsize(filename)
        print(f"{filename}: {hash}")
        if hash in files:
            files[hash].add(filename)
        else:
            files[hash] = {filename}

    for _, duplicates in files.items():
        if len(duplicates) > 1:
            duplicate_files.append(duplicates)

    return duplicate_files
