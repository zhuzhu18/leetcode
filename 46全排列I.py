def permute(nums):
    res = []
    path = []
    used = [False for _ in nums]
    dfs(nums, 0, path, res, used)
    return res


def dfs(arr, i, path, res, used):
    if i >= len(arr):
        res.append(path[:])
        return
    for j in range(len(arr)):
        if used[j] == False:
            path.append(arr[j])
            used[j] = True
            dfs(arr, i+1, path, res, used)
            path.pop()
            used[j] = False

a = [1,2,3]
b = permute(a)
print(b)
