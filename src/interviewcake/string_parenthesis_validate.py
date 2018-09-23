# O(n) time and O(p/2) where p is number of braces/brackets/parentheses in the input
def braces_brackets_parentheses_validate(code):
    code_len = len(code)

    openers_closers = {'(':')', '{':'}', '[':']'}
    opener_stack = []
    i = 0
    while i < code_len:
        if code[i] in openers_closers:
            opener_stack.append(code[i])
        elif code[i] in openers_closers.values():
            opener = opener_stack.pop()
            if not code[i] == openers_closers[opener]:
                return False

        i += 1

    return opener_stack == []
