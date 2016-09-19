from InterviewCake.word_cloud import *


def test_word_cloud0():
    string = ""
    result = {}
    wc = WordCloud(string)
    assert wc.word_cloud == result


def test_word_cloud1():
    string = "'After beating the eggs, Dana read the next step:' 'Add milk and eggs, then add flour and sugar.'"
    result = {'after': 1, 'beating': 1, 'the': 2, 'eggs': 2, 'dana': 1, 'read': 1, 'next': 1, 'step': 1, 'add': 2,
              'milk': 1, 'and': 2, 'then': 1, 'flour': 1, 'sugar': 1}
    wc = WordCloud(string)
    assert wc.word_cloud == result


def test_word_cloud3():
    string = "'ONE.,?'s:;[{]}()`!! hyphenated-word"
    result = {'ones': 1, 'hyphenated-word': 1}
    wc = WordCloud(string)
    assert wc.word_cloud == result


def test_word_cloud4():
    string = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
    result = {'we': 4, 'came': 1, 'saw': 1, 'conqueredthen': 1, 'ate': 1, 'bills': 1, 'mille-feuille': 1,
              'cake': 1}
    wc = WordCloud(string)
    assert wc.word_cloud == result
