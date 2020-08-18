def reverseVowels(s: str):
    l = 0
    r = len(s) - 1
    chrs = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    while l < r:
        while s[l] not in chrs and l < r:
            l += 1
        while s[r] not in chrs and l < r:
            r -= 1
        if l <= r:
            s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)

a = "leetcode"
b = reverseVowels(a)
print(b)