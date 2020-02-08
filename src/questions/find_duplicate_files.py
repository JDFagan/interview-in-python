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
    os.chdir(starting_dir)

    files = {}
    print(f"Finding dupe sets within {starting_dir}")
    for filename in glob.glob('**/*', recursive=True):
        if os.path.isfile(filename):
            file_hash = hash_file(filename)
            print(f"{filename}: {file_hash}")
            if file_hash in files:
                files[file_hash].add(filename)
            else:
                files[file_hash] = {filename, }

    duplicate_files = {file_hash: duplicates for (file_hash, duplicates) in files.items() if len(duplicates) > 1}
    return duplicate_files


def hash_file(filename):
    # return os.path.getsize(filename)
    with open(filename, "rb") as f:
        hasher = hashlib.md5()
        block_size = 8192
        # For Python 3.8+
        # while chunk := f.read(8192):
        chunk = f.read(block_size)
        while len(chunk) > 0:
            hasher.update(chunk)
            chunk = f.read(block_size)
    # print(hasher.digest())
    # print(hasher.hexdigest())

    return hasher.hexdigest()
