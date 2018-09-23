# Write a recursive function for generating all permutations of an input string. Return them as a set.
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.

# O(n^n) time and O(n) space
# Try to think how to handle this by hand for small string:
# cats
# result = ["cat", "cta", "atc", "act", "tac", "tca"] + s
# for cat:
#       [scat, csat, cast, cats]
# for cta:
#       [scta, csta, ctsa, ctas]
# ...


def get_permutations(s: str):
    # Base cases
    if len(s) == 1:
        return set([s])

    all_chars_except_last = s[:-1]
    last_char = s[-1]

    # recursive call
    permutations_all_chars_except_last = get_permutations(all_chars_except_last)

    permutations = set()

    # put last char in all possible positions for each above permutations
    for p in permutations_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = p[:position] + last_char + p[position:]
            permutations.add(permutation)

    return permutations

def get_permutations_s_within_b(s: str, b: str):
    s_permutations = get_permutations(s)
    len_s = len(s)

    result = set()
    for i in range(len(b) - len_s - 1):
        b_segment = b[i:i + len_s]
        print(b[i:i + len_s], end='')
        if b_segment in s_permutations:
            print('*')
            result.add(b_segment)
        else:
            print()

    return result


b = 'babcabbacaabcbabcacbb'
s = 'abbc'

b_within_s = get_permutations_s_within_b(s, b)

print()
print(s)
print(b)
print(get_permutations(s))
print(b_within_s)
