def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    area1 = (C-A)*(D-B)
    area2 = (G-E)*(H-F)
    inter = 0
    x1 = max(A, E)
    x2 = min(C, G)
    y1 = max(B, F)
    y2 = min(D, H)
    if x2 > x1 and y2 > y1:
        inter = (x2-x1)*(y2-y1)
    area = area1 + area2 - inter
    return area

a = [-3, 0, 3, 4, 0, -1, 9, 2]
b = computeArea(*a)
print(b)