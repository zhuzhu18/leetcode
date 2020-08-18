def longestPalindromeSubseq(s: str):
    if s == "":
        return 0
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

a = "cbbd"
b = longestPalindromeSubseq(a)
print(b)