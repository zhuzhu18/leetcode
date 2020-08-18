def maxProfit(prices: [int]):
    if len(prices) <= 1:
        return 0
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    return profit

a = [7, 1, 5, 3, 6, 4]
b = maxProfit(a)
print(b)