def maximalRectangle(matrix: [[str]]):
    if len(matrix) < 1:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0]*col for _ in range(row)]
    for i in range(col):
        if matrix[0][i] == '1':
            dp[0][i] = 1
    maxarea, tmp = 0, 0
    for k in range(len(matrix[0])):
        if k == 0:
            tmp = 1 if matrix[0][k] == '1' else 0
            maxarea = tmp
        elif matrix[0][k] == '1' and matrix[0][k - 1] == '1':
            tmp += 1
        elif matrix[0][k] == '1':
            tmp = 1
        else:
            maxarea = max(maxarea, tmp)
            tmp = 0
    maxarea = max(maxarea, tmp)
    for i in range(1, row):
        for j in range(col):
            if matrix[i][j] == '1':
                dp[i][j] = dp[i-1][j]+1
        for k, height in enumerate(dp[i]):
            left, right = k, k + 1
            while left >= 0 and dp[i][left] >= height:
                left -= 1
            while right < len(dp[i]) and dp[i][right] >= height:
                right += 1
            maxarea = max(maxarea, (right - left - 1) * height)
    return maxarea

a = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
b = maximalRectangle(a)
print(b)