def maxCoins(nums: [int]):
    nums = [1] + nums + [1]
    return helper(nums, 0, len(nums) - 1)

def helper(nums, left, right):
    res = 0
    if left + 1 == right:
        return res
    else:
        for i in range(left+1, right):
            res = max(res, helper(nums, left, i)+helper(nums, i, right)+nums[left]*nums[i]*nums[right])
        return res

a = [3, 1, 5, 8]
b = maxCoins(a)
print(b)