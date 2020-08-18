def longestPalindrome(s: str):
    n = len(s)
    res = 0, 0
    if n == 0:
        return ""
    if n == 1:
        pass
    elif n == 2 and s[1] == s[0]:
        res = 0, 1
    else:
        if s[1] == s[0]:
            res = 0, 1
        for i in range(1, n-1):
            odds = checkPalindrome(s, i, i)
            evens = checkPalindrome(s, i, i+1)
            if odds[1] - odds[0] > res[1] - res[0]:
                res = odds
            if evens[1] - evens[0] > res[1] - res[0]:
                res = evens
    return s[res[0]: res[1] + 1]

def checkPalindrome(s, left, right):
    if s[left] != s[right]:
        return left, left
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        left -= 1
        right += 1
    return left + 1, right - 1

a = "aaaa"
b = longestPalindrome(a)
print(b)