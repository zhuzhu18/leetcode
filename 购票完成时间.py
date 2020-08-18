def wait(nums1, nums2):
    if len(nums1) == 1:
        return nums1[0]
    nums2 = [0] + nums2
    dp = [0 for _ in nums1]
    dp[0] = nums1[0]
    dp[1] = min(nums1[0]+nums1[1], nums2[1])
    for i in range(2, len(nums2)):
        dp[i] = min(dp[i-2]+nums2[i], dp[i-1]+nums1[i])
    return dp[len(nums1)-1]

def get_time(nums1, nums2):
    wait_second = wait(nums1, nums2)
    h = wait_second // 3600
    m = (wait_second % 3600) // 60
    s = (wait_second % 3600) % 60
    res = '08:00:00 am'
    t1 = list(map(int, res.split(" ")[0].split(":")))
    t2 = res.split(" ")[1]
    hour = t1[0] + h
    minute = t1[1] + m
    second = t1[2] + s
    t1[0] = "{:0>2d}".format(hour)
    t1[1] = "{:0>2d}".format(minute)
    t1[2] = "{:0>2d}".format(second)
    if hour > 12:
        t2 = "pm"
    ans = ':'.join(t1) + " " + t2
    return ans

a = [20, 25, 18, 22, 24, 25, 26, 27, 25, 24, 23]
b = [40, 42, 41, 45, 44, 42, 46, 47, 42, 43]
c = get_time(a, b)
print(c)