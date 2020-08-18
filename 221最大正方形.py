def maximalSquare(matrix: [[str]]):
    if len(matrix) < 1:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0]*col for _ in range(row)]
    side = 0
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                dp[i][j] = 1 if matrix[i][j] == '1' else 0
            else:
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            side = max(side, dp[i][j])
    return side * side

a = [['1', '0', '1', '0', '0'],
['1', '0', '1', '1', '1'],
['1', '1', '1', '1', '1'],
['1', '0', '0', '1', '0']]
b = maximalSquare(a)
print(b)