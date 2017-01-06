

# digits = [2, 2]
# words = {'cat', 'cab', 'cats', 'aardvark', 'abacus', 'ads', 'zoo', 'hat'}
# result = {'cat', 'cab', 'cats', 'aardvark', 'abacus'}
def t9(digits, words):
    keypad = {
        1: set(),
        2: {'a', 'b', 'c'},
        3: {'d', 'e', 'f'},
        4: {'g', 'h', 'i'},
        5: {'j', 'k', 'l'},
        6: {'m', 'n', 'o'},
        7: {'p', 'q', 'r', 's'},
        8: {'t', 'u', 'v'},
        9: {'w', 'x', 'y', 'z'},
        0: set(),
    }

    result = words
    for i, digit in enumerate(digits):
        not_matched = set()
        for word in result:
            if word[i] not in keypad[digit]:
                not_matched.add(word)

        result -= not_matched

    return result
