for _ in range(int(input())):

    n, m = [int(x) for x in input().split()]

    grid = []
    for __ in range(n):
        grid.append(list(input()))

    for c in range(m):
        b = n - 1
        for r in range(n-1, -1, -1):
            if grid[r][c] == '*':
                if b != r:
                    grid[b][c] = grid[r][c]
                    grid[r][c] = '.'
                b -= 1

            if grid[r][c] == 'o':
                b = r - 1

    for r in grid:
        print("".join(r))
    
    print()
