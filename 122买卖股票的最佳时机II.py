def maxProfit(prices: [int]):
    if len(prices) <= 1:
        return 0
    profit = 0
    i, j = 0, 0
    while i < len(prices):
        while i+1 < len(prices) and prices[i+1] <= prices[i]:
            i += 1      # 找谷底的位置
        j = i
        while j+1 < len(prices) and prices[j+1] >= prices[j]:
            j += 1      # 找谷底后第一个峰值的位置
        profit += (prices[j] - prices[i])
        i = j + 1
    return profit

a = [7, 1, 5, 3, 6, 4]
b = maxProfit(a)
print(b)