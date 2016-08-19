from InterviewCake.coin_combos import *
import pytest


def test_coins1():
    amount = 4
    coins = [1, 2, 3]
    result = [
        [3]*1, [1]*1
        , [2]*2
        , [1]*4
    ]
    assert get_coin_combos(amount=amount, coins=coins) == len(result)


def test_coins2():
    amount = 10
    coins = [1, 5, 10, 25, 50, 100]
    result = [
        [10] * 1
        , [5] * 2
        , [5] * 1 + [1] * 5
        , [1] * 10
    ]
    assert get_coin_combos(amount=amount, coins=coins) == len(result)
