import os
import glob

import hashlib


def find_duplicate_files(starting_dir: str = os.path.abspath(os.curdir)):
    """
    Insight: dupes will definitely have same file size and have same hash of its contents.

    Strategy: In consideration of very large files potentially within a directory, it will be much faster to first
    filter out only files with same file size first before obtaining the hash for each duplicate file candidate since
    very large files will take quite some time to hash.

    Time complexity
    O(n + S)
    where
      - n is number of input files
      - S is sizes of duplicate files in aggregate

    Space complexity
    O(n + d)
    where
      - n is number of input files
      - d is number of duplicate files

    :param starting_dir: path as string
    :return: dictionary of unique file hashes where each hash is associated to the set of files that match that hash
    """
    os.chdir(starting_dir)

    # file_sizes and file_hashes are dictionaries similar in structure where key is only difference (file size vs.
    # file hash) and values are same - sets of filenames that match that key:
    #   {
    #     key1: {filename1, filename2, ...},
    #     key2: {filename0, }
    #     ...
    #   }

    # File size pass
    file_sizes = {}
    print(f"Finding dupe candidates within {starting_dir}")
    for filename in glob.glob('**/*', recursive=True):
        if os.path.isfile(filename):
            file_size = os.path.getsize(filename)
            print(f"{filename}: {file_size}")
            if file_size in file_sizes:
                file_sizes[file_size].add(filename)
                print(f"{filename} is possible dupe")
            else:
                file_sizes[file_size] = {filename, }

    # Filter the duplicate candidates to speed up hashing only files we really need to hash
    duplicate_candidates = set()
    for _, duplicates in file_sizes.items():
        if len(duplicates) > 1:
            duplicate_candidates |= duplicates

    # Hash pass
    file_hashes = {}
    print(f"Finding exact dupes within {starting_dir}")
    for filename in duplicate_candidates:
        if os.path.isfile(filename):
            file_hash = hash_file(filename)
            print(f"{filename}: {file_hash}")
            if file_hash in file_hashes:
                file_hashes[file_hash].add(filename)
            else:
                file_hashes[file_hash] = {filename, }

    duplicate_files = {file_hash: duplicates for (file_hash, duplicates) in file_hashes.items() if len(duplicates) > 1}
    return duplicate_files


def hash_file(filename):
    # return os.path.getsize(filename)
    with open(filename, "rb") as f:
        hasher = hashlib.md5()
        # hasher.update(f.read())
        block_size = 2**16
        # For Python 3.8+
        # while chunk := f.read(8192):
        chunk = f.read(block_size)
        while len(chunk) > 0:
            hasher.update(chunk)
            chunk = f.read(block_size)
    return hasher.hexdigest()
