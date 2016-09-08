# O(n) time and O(1) space
def match(input, parens_position):
    input_len = len(input)
    if parens_position < 0 or parens_position > input_len - 1 or input[parens_position] != "(":
        raise IndexError("Parenthesis position index error - no parens at that location")

    parens_open_count = 0
    i = parens_position + 1
    while i < input_len:
        if input[i] == "(":
            parens_open_count += 1
        elif input[i] == ")":
            if parens_open_count == 0:
                return i
            parens_open_count -= 1
        i += 1

    return None
