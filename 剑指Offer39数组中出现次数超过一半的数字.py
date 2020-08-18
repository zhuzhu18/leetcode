from typing import List

def majorityElement(nums: List[int]):
    major = 0
    count = 0
    for n in nums:
        if count == 0 or n == major:
            major = n
            count += 1
        else:
            count -= 1
    return major

a = [3, 2, 4, 2, 2, 3, 2]
b = majorityElement(a)
print(b)