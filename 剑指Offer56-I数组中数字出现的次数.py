def singleNumbers(nums: [int]):
    ret = nums[0]
    for i in nums[1:]:
        ret ^= i        # 所有数异或结果为不同的两数异或结果
    j = 1
    while ret & j == 0:       # 找到第一个二进制为1的位
        j = j << 1
    a, b = 0, 0
    for k in nums:
        if k & j != 0:       # 与j的不为0的二进制一样的数做为一组
            a = a ^ k
        else:                # 与j的不为0的二进制不同的数做为一组
            b = b ^ k
    return [a, b]

a = [1, 2, 10, 4, 1, 4, 3, 3]
b = singleNumbers(a)
print(b)