def get_max_profit(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    # Greedy solution requiring O(n) time and O(1) space
    for i, current_price in enumerate(stock_prices_yesterday):
        if i == 0:
            continue

        profit = current_price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, current_price)

    return max_profit
