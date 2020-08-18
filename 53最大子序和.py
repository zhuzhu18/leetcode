def maxSubArray(nums: [int]):
    if len(nums) == 1:
        return nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
b = maxSubArray(a)
print(b)