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
    return change_possibilities_top_down(amount, coins)


def change_possibilities_top_down(amount_left, denominations_left):

    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0:
        return 1
    # we overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0
    # we're out of denominations
    if len(denominations_left) == 0:
        return 0

    print(str.format("checking ways to make {} with {}", amount_left, denominations_left))

    # choose a current coin
    current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    possibilities = {}
    num_possibilities = 0
    while amount_left >= 0:
        if possibilities.get(amount_left) is None:
            possibilities[amount_left] = change_possibilities_top_down(amount_left, rest_of_coins)
        num_possibilities += possibilities[amount_left]
        # num_possibilities += change_possibilities_top_down(amount_left, rest_of_coins)
        amount_left -= current_coin
        # print(str.format("({}): checking ways to make {} with {}", num_possibilities, amount_left, denominations_left))

    return num_possibilities
