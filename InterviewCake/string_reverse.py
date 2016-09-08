# O(n/2) time and O(n) space
def reverse_string(s):
    if s is None:
        return None

    chars = list(s)

    ceiling_index = len(chars)
    # swap in place high indices with low indices
    for i in range(ceiling_index//2):
        temp = chars[i]
        chars[i] = chars[ceiling_index - 1 - i]
        chars[ceiling_index - 1 - i] = temp

    # rebuild back the reversed string
    return ''.join(chars)
