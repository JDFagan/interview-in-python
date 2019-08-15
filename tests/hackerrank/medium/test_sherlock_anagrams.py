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
    assert len(sherlockAndAnagrams('abba')) == 4
    assert len(sherlockAndAnagrams('abcd')) == 0
    assert len(sherlockAndAnagrams('ifailuhkqq')) == 3
    assert len(sherlockAndAnagrams('kkkk')) == 10
