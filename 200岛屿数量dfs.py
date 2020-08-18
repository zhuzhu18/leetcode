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
                grid[i][j] = '0'
                dfs(grid, i, j)

    return count

def dfs(grid, i, j):
    row = len(grid)
    col = len(grid[0])
    directions = {'up': [i-1, j], 'down': [i+1, j], 'left': [i, j-1], 'right': [i, j+1]}
    for pos in directions.values():
        if pos[0] >= 0 and pos[0] < row and pos[1] >= 0 and pos[1] < col and grid[pos[0]][pos[1]] == '1':
            grid[pos[0]][pos[1]] = '0'
            dfs(grid, pos[0], pos[1])

a = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
b = numIslands(a)
print(b)