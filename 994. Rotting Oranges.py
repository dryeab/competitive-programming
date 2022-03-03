class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def canBeRotten(r, c):
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and grid[nr][nc] == 2:
                    return True
            return False
        
        min = 0 # minute
        
        while True:
            
            f, store = 0, [] # no of fresh oranges, oranges to become rotten
            
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        f += 1
                        if canBeRotten(r, c):
                            # print('to rote', r, c, min)
                            store.append((r,c))
            
            for r, c in store:
                grid[r][c] = 2
                
            if not f:
                return min
            
            if not store:
                return -1
            
            min += 1