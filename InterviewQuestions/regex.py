# aabbbbbbbbcde aab*.de == True
def match(str, regex):
    result = True

    for s in range(len(str)):
        for r in range(len(regex)):
            if str[s] == regex[r]:
                continue

    return result

assert match('abc', 'abc') == True