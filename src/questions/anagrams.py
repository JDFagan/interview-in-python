import itertools


def get_anagrams(s):
    ["".join(perm) for perm in itertools.permutations(s)]


def get_anagrams2(s):
    if len(s) <= 1:
        yield s
    else:
        for perm in get_anagrams2(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + s[0:1] + perm[i:]


def get_anagrams3(s):
    if len(s) <= 1:
        return s
    else:
        tmp = []
        for perm in get_anagrams3(s[1:]):
            for i in range(len(s)):
                tmp.append(perm[:i] + s[0:1] + perm[i:])
        return tmp
