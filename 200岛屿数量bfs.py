def numIslands(grid: [[str]]):
    count = 0
    if len(grid) == 0:
        return count
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                count += 1
                bfs(grid, i, j)

    return count

def bfs(grid, i, j):
    row = len(grid)
    col = len(grid[0])
    directions = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    queue = []
    queue.append([i, j])
    while queue:
        tmp = queue.pop()
        grid[tmp[0]][tmp[1]] = '0'
        for direction in directions.values():
            pos = [tmp[0]+direction[0], tmp[1]+direction[1]]
            if pos[0] >= 0 and pos[0] < row and pos[1] >= 0 and pos[1] < col and grid[pos[0]][pos[1]] == '1':
                queue.append(pos)

a = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
b = numIslands(a)
print(b)