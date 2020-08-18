def maxSubArray(nums: [int]):
    max_i = nums[0]      # 以第i位结束的最大乘积
    min_i = nums[0]      # 以第i位结束的最小乘积, 有可能为负数
    res = max_i
    for i in range(1, len(nums)):
        tmp = max_i
        max_i = max(tmp*nums[i], min_i*nums[i], nums[i])
        min_i = min(tmp*nums[i], min_i*nums[i], nums[i])
        res = max(res, max_i)
    return res

a = [-4, -3, -2]
b = maxSubArray(a)
print(b)