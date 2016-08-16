def get_max_profit(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = max_price = None
    profit = max_profit = None

    # Greedy solution requiring O(n) time and O(1) space
    for i in range(len(stock_prices_yesterday)):
        if i == 0:
            min_price = i
            continue

        if max_price is None or stock_prices_yesterday[i] > stock_prices_yesterday[max_price]:
            max_price = i

        # print("i = " + i)
        profit = stock_prices_yesterday[max_price] - stock_prices_yesterday[min_price]
        if max_profit is None or profit > max_profit:
            max_profit = profit

        if stock_prices_yesterday[i] < stock_prices_yesterday[min_price]:
            min_price = i
            max_price = None

    return max_profit
