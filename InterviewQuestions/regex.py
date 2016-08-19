# aabbbbbbbbcde aab*.de == True
def match(string, regex):
    result = True
    prev = None

    s = r = 0
    while s <= len(string) - 1 and r <= len(regex) - 1:
        if string[s] == regex[r]:
            s += 1
            r += 1
        # elif regex[r] == '.':
        #     r += 1
        #     pass

        prev = r

    return result
