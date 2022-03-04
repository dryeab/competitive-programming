class Solution:
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n, DIR = len(grid), [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n 
        hasReached = lambda r, c: r == c == n - 1
        
        heap = [(0, 0, 0)]
        
        while True:
            
            t, r, c = heapq.heappop(heap)
            
            if hasReached(r, c):
                return t
            
            if grid[r][c] != None:
                
                for d in DIR:
                    nr, nc = r + d[0], c + d[1]
                    if inBound(nr, nc) and grid[nr][nc] != None:
                        nt = t + max(0, max(grid[r][c], grid[nr][nc]) - t)
                        heapq.heappush(heap, (nt, nr, nc))
            
                grid[r][c] = None