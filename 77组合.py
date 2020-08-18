def combine(n: int, k: int):
    res = []
    path = []
    nums = [i for i in range(1, n+1)]
    backtrack(nums, res, path, k, 0)
    return res

def backtrack(nums, res, path, k, start):
    if len(path) == k:
        res.append(path[:])
        return
    if start >= len(nums):
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, res, path, k, i+1)
        path.pop()

n = 4
k = 2
a = combine(n, k)
print(a)