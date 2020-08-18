def maxProfit(prices: [int]):
    if len(prices) <= 1:
        return 0
    min_price = prices[0]
    profit = 0
    for p in prices:
        if p <= min_price:
            min_price = p
        else:
            profit = max(profit, p - min_price)
    return profit

a = [7, 1, 5, 3, 6, 4]
b = maxProfit(a)
print(b)