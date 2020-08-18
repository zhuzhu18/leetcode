def findSubsequences(nums: [int]) -> [[int]]:
    cur = ()
    res = set()
    dfs(nums, cur, res, 0)
    return res

def dfs(nums, cur, res, i):
    if len(cur) >= 2 and cur not in res:
        res.add(cur)
    if i >= len(nums):
        return
    if len(cur) == 0 or nums[i] >= cur[-1]:
        cur = cur + (nums[i], )
        dfs(nums, cur, res, i + 1)
        cur = cur[:-1]
    dfs(nums, cur, res, i + 1)

a = [4, 6, 7, 7]
b = findSubsequences(a)
print(b)