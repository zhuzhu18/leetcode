def rob(nums: [int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) == 3:
        return max(nums[1], nums[0]+nums[2])
    dp = [0 for _ in nums]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    dp[2] = max(nums[1], nums[0] + nums[2])
    for i in range(3, len(nums)):
        dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i-1])
    return dp[-1]

a = [2, 7, 9, 3, 1]
b = rob(a)
print(b)