# O(n) time and O(u) space where u is unique letters in the input
def has_palindrome(word: str):
    letter_is_odd = {}

    for char in word:
        if char in letter_is_odd:
            # Toggle odd-ness of existing letter
            letter_is_odd[char] = not letter_is_odd[char]
        else:
            # First instance of letter found means its odd count of this letter
            letter_is_odd[char] = True

    odd_letters = 0
    word_must_have_odd = not len(word) % 2 == 0

    for odds in letter_is_odd.values():
        if odds:
            odd_letters += 1

    if word_must_have_odd:
        return odd_letters == 1
    else:
        return odd_letters == 0
