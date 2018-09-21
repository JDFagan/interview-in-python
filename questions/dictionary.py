"""
Implement a hash table with arrays.
"""

class Dictionary:
    """
    A hash table is an array of arrays.  The outer array's index refers to the "hashed" index generated from a given
    key.  Two different keys could potentially hash to the same index.  To handle this collision, the inner array
    is used.  As long as hash functions evenly distribute keys, O(1) retrieval should be possible as long not too many
    keys are stored with regards to overall size of hash table.  Size of hash table can be increased to affect this
    performance of retrieval - generically the performance is O(n/m) where n is universe of all keys possible and m
    is size of hash table.  For example, if universe keys possible are 100 and hash table is only 10 size, then on
    average, O(100/10) = O(10) which is still sub-linear speed.
    """
    def __init__(self, size=100):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        key_index = self._hash(key)
        bucket = self.data[key_index]
        if not bucket:
            bucket.append((key, value))
        else:
            # Handle hash collision
            for i, kv in enumerate(bucket):
                if kv[0] == key:
                    bucket[i] = (key, value)
                    break

    def __getitem__(self, key):
        key_index = self._hash(key)
        bucket = self.data[key_index]
        value = None
        for kv in bucket:
            if kv[0] == key:
                value = kv[1]
                break
        return value

    def __delitem__(self, key):
        key_index = self._hash(key)
        bucket = self.data[key_index]
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket.remove(kv)
                break

    def _hash(self, key):
        return hash(key) % self.size
