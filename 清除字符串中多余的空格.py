def clean_str(s: str):
    s = s.strip()
    left = 0
    while left < len(s):
        if s[left] != ' ':
            left += 1
            continue
        right = left + 1
        while s[right] == s[left]:
            right += 1
        s = s.replace(s[left: right], ' ')
        left += 1
    return s

def clean_str2(s: str):
    s = s.strip()
    left, right = 0, 0
    ls = []
    while left < len(s):
        while left < len(s) and s[left] != ' ':
            left += 1
        if left >= len(s):
            break
        right = left
        while s[right] == s[left]:
            right += 1
        ls.append([left, right])
        left = right
    l = 0      # 删除的长度
    for i, j in ls:
        s = s.replace(s[i-l:j-l], ' ', 1)
        l = j - i - 1
    return s

test = "       egfhhe  vfj     dbk  "
print(clean_str(test))