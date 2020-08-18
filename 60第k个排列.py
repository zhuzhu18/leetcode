import math

def getPermutation(n: int, k: int):
    k -= 1
    nums = [i for i in range(1, n+1)]
    fac = [math.factorial(j) for j in range(n-1, -1, -1)]
    coef = []
    for m in range(n):
        coef.append(k//fac[m])
        k = k % fac[m]
    res = ""
    for t in range(n):
        res += str(nums.pop(coef[t]))
    return res

a = getPermutation(3, 3)
print(a)