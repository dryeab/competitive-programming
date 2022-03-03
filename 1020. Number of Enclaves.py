class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m, n, visited = len(grid), len(grid[0]), set()
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def markRegion(r, c):
            visited.add((r,c))
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    markRegion(nr, nc)
        
        # mark the boarders first
        for r in [0, m-1]:
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    markRegion(r, c)
                    
        for c in [0, n-1]:
            for r in range(m):
                if grid[r][c] == 1 and (r, c) not in visited:
                    markRegion(r, c)
        
        answer = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    answer += 1
        
        return answer
                    