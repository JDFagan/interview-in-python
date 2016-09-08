# O(n) time and O(u) space where u is unique letters in the input
def has_palindrome(word: str):
    unpaired_letters = set()

    for char in word:
        if char in unpaired_letters:
            unpaired_letters.remove(char)
        else:
            unpaired_letters.add(char)

    return len(unpaired_letters) <= 1
