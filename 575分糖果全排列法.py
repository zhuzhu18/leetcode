def distributeCandies(candies: [int]):
    def permute(nums, i):
        nonlocal max_kind
        if i >= len(nums):
            hashset = set()
            for k in range(len(nums)//2):
                hashset.add(nums[k])
            max_kind = len(hashset) if len(hashset) > max_kind else max_kind
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            permute(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
    max_kind = 0
    permute(candies, 0)
    return max_kind

a = [2, 1, 2, 1, 2, 1, 2, 1]
b = distributeCandies(a)
print(b)