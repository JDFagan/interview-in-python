# O(n) time and O(n) space
def reverse_words(message: str):
    if message is None:
        return None

    words = message.split(' ')

    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return ' '.join(words)
