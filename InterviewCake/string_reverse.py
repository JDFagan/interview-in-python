# O(n) time and O(n) space
def reverse_string(s):
    if s is None:
        return None

    chars = list(s)
    left = 0
    right = len(chars) - 1

    # swap in place high indices with low indices
    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp
        left += 1
        right -= 1

    # rebuild back the reversed string
    return ''.join(chars)
