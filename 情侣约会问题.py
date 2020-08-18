def dating_problem(nums):
    existed = set()
    swapnum = 0
    k = 0
    while k < len(nums):
        if nums[k] in existed:
            continue
        for j in range(k+1, len(nums)):
            if nums[j] == nums[k]:
                break
            swapnum += 1
        nums.pop(j)      # 退出循环时nums[j]与nums[k]构成情侣, 由于要将她移到j+1位置, 所以将她删除
        existed.add(nums[k])
        k += 1
    return swapnum

a = [1, 2, 3, 4, 1, 2, 3, 4]
b = dating_problem(a)
print(b)