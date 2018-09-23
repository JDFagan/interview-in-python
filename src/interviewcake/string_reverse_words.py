from interviewcake.string_reverse import *


# O(n) time and O(n) space
def reverse_words(message: str):
    if message is None:
        return None
    if message == "":
        return ""

    reverse_message = reverse_string(message)
    chars = list(reverse_message)

    left = 0
    for right in range(len(chars)):
        if chars[right] == ' ':
            # found word boundary, so reverse that word
            chars[left:right] = reverse_string(''.join(chars[left:right]))
            left = right + 1

    # Reverse chars of last word which doesn't have a space at the end
    chars[left:right+1] = reverse_string(''.join(chars[left:right+1]))

    return ''.join(chars)
