# aabbbbbbbbcde aab*.de == True
def match(string, regex):
    result = True
    prev = None

    s = r = 0
    while s <= len(string) - 1 and r <= len(regex) - 1:
        if regex[r] == '.':
            s += 1
            prev = r
            r += 1
        elif regex[r] == '*':
            if string[s] == regex[prev]:
                s += 1
            else:
                prev = r
                r += 1
        elif string[s] == regex[r]:
            s += 1
            prev = r
            r += 1
        else:
            result = False
            break

    if result and (s != len(string) or r != len(string)):
        if s == len(string) and r == len(regex) - 1 and regex[r] == '*':
            result = True
        else:
            result = False

    return result
