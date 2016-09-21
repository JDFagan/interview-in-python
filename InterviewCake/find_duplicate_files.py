import glob
import os
from hashlib import md5


# O(n) time and O(n) space
def find_duplicate_files(starting_dir: str):
    # Strategy: dups will definitely have same file size and should have same hash of its contents
    # files[hash] = ('/path/to/file' created_date)

    result = []
    files = {}

    for filename in glob.iglob(starting_dir + '/**/*.*', recursive=True):
        # print(filename)
        with open(filename, 'rb') as f:
            created_date = os.path.getctime(filename)
            data = f.read()
            hexhash = md5(data).hexdigest()

            if hexhash in files:
                # We have a dup
                # Created Time tells us which file is the original
                if created_date < files[hexhash][1]:
                    result.append((filename, files[hexhash][0]))
                else:
                    result.append((files[hexhash][0], filename))
            else:
                # No dup, so add file to files hashtable
                files[hexhash] = (filename, created_date)

    return result
