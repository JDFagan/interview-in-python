# O(n) time and O(u) space where u is unique letters in the input.  It's possible to think that the
# unique letters at worse is a constant number (e.g., only a 100k Unicode characters), so, one could
# say its actually O(1) space.
def has_palindrome(word: str):
    unpaired_letters = set()

    for char in word:
        if char in unpaired_letters:
            unpaired_letters.remove(char)
        else:
            unpaired_letters.add(char)

    return len(unpaired_letters) <= 1
