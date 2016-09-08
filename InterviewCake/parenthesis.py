# O(n) time and O(n) space
def match(input, parens_position):
    input_len = len(input)
    if parens_position < 0 or parens_position > input_len - 1 or input[parens_position] != "(":
        raise IndexError("Parenthesis position index error - no parens at that location")

    parens_stack = []
    chars = list(input)
    i = parens_position + 1
    while i < input_len:
        if chars[i] == "(":
            parens_stack.append(1)
        elif chars[i] == ")":
            if parens_stack == []:
                return i
            parens_stack.pop()
        i += 1

    return None
