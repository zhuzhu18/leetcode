def candy(ratings: [int]):
    candies = [1 for _ in ratings]
    for i in range(1, len(candies)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1
    count = candies[-1]
    for j in range(len(ratings)-2, -1, -1):
        if ratings[j] > ratings[j+1]:        # 若ratings[j]<ratings[j+1], 在前一次循环中已处理, 无需更新candies[j]
            candies[j] = max(candies[j], candies[j+1]+1)    # 在第一个循环中有可能使candies[j]变得很大, 但candies[j+1]却很小
        count += candies[j]
    return count

a = [1, 3, 4, 5, 2]
b = candy(a)
print(b)