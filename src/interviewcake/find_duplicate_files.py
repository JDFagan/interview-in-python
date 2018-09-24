import os
import glob

from hashlib import md5


def find_duplicate_files(starting_dir: str):
    """
    Strategy: dups will definitely have same file size and should have same hash of its contents
        files[hash] = ('/path/to/file', created_date)

    O(n) time and O(n + d) space (where n in input files and d is number of duplicate files).

    :param starting_dir: path as string
    :return: list of tuples where each tuple represents pair of duplicate files
    """
    files = {}
    duplicate_files = []

    for filename in glob.iglob(starting_dir + '/**/*.*', recursive=True):
        with open(filename, 'rb') as f:
            created_date = os.path.getctime(filename)
            data = f.read()

        hexhash = md5(data).hexdigest()
        print('(path, created_date, hexhash) = ({}, {}, {})'.format(filename, created_date, hexhash))

        if hexhash not in files:
            # No dup, so add file to files hashtable
            files[hexhash] = (filename, created_date)
            print('  hexhash ({}) not found in files'.format(hexhash))
        else:
            # We have a dup - Created Time tells us which file is the original
            prior_filename = files[hexhash][0]
            prior_created_date = files[hexhash][1]
            if created_date < prior_created_date:
                duplicate_files.append((filename, prior_filename))
                print('  dupe detected: (filename = {}, prior_filename = {})'.format(filename, prior_filename))
            else:
                duplicate_files.append((prior_filename, filename))
                print('  dupe detected: (prior_filename = {}, filename = {})'.format(prior_filename, filename))

    return duplicate_files
