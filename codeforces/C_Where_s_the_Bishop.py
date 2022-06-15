def solve(grid):
    for i in range(1, 8):
        for j in range(1, 8):
            if grid[i][j] == '#':
                if grid[i-1][j-1] == '#' and grid[i-1][j+1] == '#' and grid[i+1][j+1] == '#' and grid[i+1][j-1] == '#':
                    return i + 1, j + 1


for _ in range(int(input())):
    input()
    grid = [input() for _ in range(8)]
    print(*solve(grid))
