res = 0
def numTrees(n: int):
    dp = [0 for _ in range(n+1)]
    dp[0] = dp[1] = 1
    if n < 2:
        return dp[n]
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    return dp[n]
a = 1
b = numTrees(a)
print(b)