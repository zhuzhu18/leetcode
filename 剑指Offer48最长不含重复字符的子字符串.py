def lengthOfLongestSubstring(s: str):
    res = set()
    stack = []
    ans = 0
    for c in s:
        if c not in res:
            stack.append(c)
            res.add(c)
            ans = max(ans, len(stack))
        else:
            ans = max(ans, len(res))
            i = stack.index(c)
            stack = stack[i+1:]
            stack.append(c)
            res = set(stack)
    return ans

a = "nfpdmpi"
b = lengthOfLongestSubstring(a)
print(b)