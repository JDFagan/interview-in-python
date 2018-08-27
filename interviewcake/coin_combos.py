# given: an amount of money, a list of coin denominations
# computes the number of ways to make amount of money with coins of the available denominations.
def coin_combos(amount, coins):
    if amount < 0:
        return []
    if amount == 0:
        return [[]]

    result = []
    for coin in coins:
        combos = coin_combos(amount - coin, coins)
        # for combo in combos:
        #     combo.append(coin)
        result.append(combos)

    return result


def get_coin_combos(amount, coins):
    return change_possibilities_bottom_up(amount, coins)


# O(n*m) time and O(n) space
def change_possibilities_bottom_up(amount, coins):
    ways_of_n = [0] * (amount + 1)
    ways_of_n[0] = 1

    for coin in coins:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_n[higher_amount] += ways_of_n[higher_amount_remainder]
            print(str.format("checking ways to make {} with {}", higher_amount, coin))

    return ways_of_n[amount]


# O(n*m) time and O(n*m) space - extra m space due to call stack of recursion
def change_possibilities_top_down(amount, coins):

    # base cases:
    # we hit the amount spot on. yes!
    if amount == 0:
        return 1
    # we overshot the amount left (used too many coins)
    if amount < 0:
        return 0
    # we're out of denominations
    if len(coins) == 0:
        return 0

    print(str.format("checking ways to make {} with {}", amount, coins))

    # choose a current coin
    current_coin, rest_of_coins = coins[0], coins[1:]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    possibilities = {}
    num_possibilities = 0
    while amount >= 0:
        if possibilities.get(amount) is None:
            possibilities[amount] = change_possibilities_top_down(amount, rest_of_coins)
        num_possibilities += possibilities[amount]
        # num_possibilities += change_possibilities_top_down(amount_left, rest_of_coins)
        amount -= current_coin
        # print(str.format("({}): checking ways to make {} with {}", num_possibilities, amount_left, denominations_left))

    return num_possibilities
