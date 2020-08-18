def distributeCandies(candies: [int]):
    kinds = 0      # 得到的糖果种类数
    i = 0
    while i < len(candies) and kinds < len(candies) // 2:
        if candies[i] != -float('inf'):      # 如果当前糖果为无效值, 即在前面出现过该种类, 则跳过当前糖果
            kinds += 1
            for j in range(i+1, len(candies)):
                if candies[j] == candies[i]:
                    candies[j] = -float('inf')        # 如果这颗糖果在前面出现过则标记为无效值
        i += 1
    return kinds
a = [2, 1, 2, 1, 2, 1, 2, 1]
b = distributeCandies(a)
print(b)