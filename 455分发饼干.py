def findContentChildren(g: [int], s: [int]):
    g.sort()
    s.sort()
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
            j += 1
        else:
            j += 1
    return i

a = [5, 4]
b = [1, 2, 3]
c = findContentChildren(a, b)
print(c)