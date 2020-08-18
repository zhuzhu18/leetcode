def combine(nums: [int]):
    res = []
    path = []
    backtrack(nums, res, path, 0)
    return res

def backtrack(nums, res, path, start):
    res.append(path[:])
    if start >= len(nums):
        return res
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, res, path, i+1)
        path.pop()

a = [1, 2, 3]
a = combine(a)
print(a)