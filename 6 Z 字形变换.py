def convert(s: str, numRows: int):
    ls = ["" for _ in range(numRows)]         # 存储每行的字符串
    down = False
    i = 0
    for c in s:
        if i >= numRows-1:    # 达到最末尾行就开始上升
            down = False
        elif i <= 0:          # 达到首行就开始下降
            down = True
        if down:
            ls[i] += c
            i += 1
        else:
            ls[i] += c
            i -= 1
    return ''.join(ls)

a = "LEETCODEISHIRING"
b = 4
c = convert(a, b)
print(c)