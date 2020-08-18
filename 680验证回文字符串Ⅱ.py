def validPalindrome(s: str):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return isPalindrome(s[l: r]) or isPalindrome(s[l+1: r+1])
        l += 1
        r -= 1
    return True

def isPalindrome(s: str):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

s = 'abcdba'
b = validPalindrome(s)
print(b)