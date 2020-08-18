def removeElement(nums: [int], val: int):
    i = 0
    for k in nums:
        if k != val:
            nums[i] = k
            i += 1
    return i

a = [0, 1, 2, 2, 3, 0, 4, 2]
b = 2
c = removeElement(a, b)
print(c)