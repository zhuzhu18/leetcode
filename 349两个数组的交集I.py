def intersection(nums1, nums2):
    p1 = p2 = 0
    res = []
    nums1.sort()
    nums2.sort()
    while p1 < len(nums1) and p2 < len(nums2):
        if p1 > 0 and nums1[p1] == nums1[p1-1]:
            p1 += 1
            continue
        if p2 > 0 and nums2[p2] == nums2[p2-1]:
            p2 += 1
            continue
        if nums1[p1] == nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return res

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

a = intersection(nums1, nums2)
print(a)