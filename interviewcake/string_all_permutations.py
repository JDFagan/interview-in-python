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
def get_permutations(string: str):
    # Base cases
    if len(string) == 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call
    permutations_all_chars_except_last = get_permutations(all_chars_except_last)

    permutations = set()

    # put last char in all possible positions for each above permutations
    for p in permutations_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = p[:position] + last_char + p[position:]
            permutations.add(permutation)

    return permutations
