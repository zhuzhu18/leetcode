def findMin(nums: [int]):
    n = len(nums)
    left, right = 0, n-1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]

a = [4, 5, 6, 7, 0, 1, 2]
b = findMin(a)
print(b)