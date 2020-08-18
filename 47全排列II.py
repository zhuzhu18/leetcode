def permute(nums):
    res = []
    path = []
    used = [False for _ in nums]
    nums.sort()
    dfs(nums, 0, path, res, used)
    return res

def dfs(arr, i, path, res, used):
    if i >= len(arr):
        res.append(path[:])
        return
    for j in range(len(arr)):
        if j > 0 and arr[j] == arr[j-1] and used[j-1] == False:
            continue
        if used[j] == False:
            path.append(arr[j])
            used[j] = True
            dfs(arr, i+1, path, res, used)
            path.pop()
            used[j] = False

a = [1,2,1]
b = permute(a)
print(b)