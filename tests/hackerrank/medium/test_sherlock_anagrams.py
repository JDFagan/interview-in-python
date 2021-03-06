from hackerrank.medium.sherlock_anagrams import is_anagram, get_substrings, sherlockAndAnagrams


def test_is_anagram():
    assert is_anagram('a', 'a')
    assert is_anagram('ab', 'ba')
    assert is_anagram('abb', 'bba')
    assert not is_anagram('ab', 'cd')
    assert not is_anagram('abb', 'aba')
    assert is_anagram('ab', 'ab')
    assert is_anagram('abb', 'abb')
    assert is_anagram('anagram', 'nagaram')


def test_get_substrings():
    print(get_substrings('abba'))


def test_sherlock_and_anagrams():
    assert sherlockAndAnagrams('abba') == 4
    assert sherlockAndAnagrams('abcd') == 0
    assert sherlockAndAnagrams('ifailuhkqq') == 3
    assert sherlockAndAnagrams('kkkk') == 10
    assert sherlockAndAnagrams('cdcd') == 5

def test_sherlock_and_anagrams_long():
    assert sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel') == 399
    assert sherlockAndAnagrams('gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde') == 471
