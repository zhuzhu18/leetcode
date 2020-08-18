def lengthOfLIS(nums: [int]):
    if len(nums) <= 1:
        return len(nums)
    dp = [1] * len(nums)
    res = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
        res = max(res, dp[i])
    return res

a = [1, 3, 6, 7, 9, 4, 10, 5, 6]
b = lengthOfLIS(a)
print(b)