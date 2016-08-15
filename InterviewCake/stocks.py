def get_max_profit(stock_prices_yesterday):
    min_price = max_price = None
    profit = max_profit = None
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
