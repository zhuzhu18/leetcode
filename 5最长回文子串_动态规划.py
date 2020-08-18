def longestPalindrome(s: str):
    n = len(s)
    dp = [[True for _ in range(n)] for _ in range(n)]
    res = (0, 0)

    if n == 2 and s[1] == s[0]:
        res = (0, 1)

    for i in range(n-1):
        dp[i][i+1] = (s[i] == s[i+1])
        if dp[i][i+1]:
            res = (i, i+1)

    for col in range(2, n):
        for row in range(col-1):
            dp[row][col] = (s[row] == s[col] and dp[row+1][col-1])
            if dp[row][col] and (col - row > res[1] - res[0]):
                res = (row, col)
    return s[res[0]: res[1]+1]

a = "babad"
b = longestPalindrome(a)
print(b)