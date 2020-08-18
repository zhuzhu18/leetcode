def lengthOfLongestSubstring(s: str):
    occur = dict()
    maxlen = 0
    start = 0
    for i, c in enumerate(s):
        if c not in occur:
            occur[c] = i
        else:
            maxlen = max(maxlen, i-start)
            start = max(start, occur[c]+1)     # 注意更新窗口的起始位置, 当前重复字符出现的位置可能在窗口起始位置之前, 所以取最大值
            occur[c] = i      # 更新重复字符的位置为当前位置
    maxlen = max(maxlen, len(s)-start)     # 遍历结束时可能最后几个字符都不是重复的, 所以再计算一次窗口开始位置到最后字符的长度
    return maxlen

a = "pwwkew"
b = lengthOfLongestSubstring(a)
print(b)