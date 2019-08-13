open_parens = ["[", "{", "("]
close_parens = ["]", "}", ")"]


# Question by Dropbox
def is_parens_balanced(string: str):
    stack = []
    for c in string:
        if c in open_parens:
            stack.append(c)
        elif c in close_parens:
            parens_index = close_parens.index(c)
            if len(stack) > 0 and open_parens[parens_index] == stack[-1]:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False

    return True


assert is_parens_balanced('()')
assert is_parens_balanced('(123)')
assert is_parens_balanced('(((abc)(123)2)3)')
assert not is_parens_balanced('((()())')
assert not is_parens_balanced('(()()))')
assert not is_parens_balanced('(]')
assert is_parens_balanced('{((abc)[123]2)3}')
