def twoSum(numbers: [int], target: int):
    left, right = 0, len(numbers)-1
    while left < right:
        tmp = numbers[left] + numbers[right]
        if tmp == target:
            break
        elif tmp > target:
            right -= 1
        else:
            left += 1
    return [left+1, right+1]

a = [2, 7, 11, 15]
b = 9
c = twoSum(a, b)
print(c)