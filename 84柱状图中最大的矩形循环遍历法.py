def largestRectangleArea(heights: [int]):
    maxarea = 0
    for i, height in enumerate(heights):
        left, right = i, i+1
        while left >= 0 and heights[left] >= height:
            left -= 1
        while right < len(heights) and heights[right] >= height:
            right += 1
        maxarea = max(maxarea, (right-left-1)*height)
    return maxarea

a = [2, 1, 5, 6, 3]
b = largestRectangleArea(a)
print(b)