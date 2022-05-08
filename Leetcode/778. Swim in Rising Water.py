
# Link - https://leetcode.com/problems/swim-in-rising-water/

# Space: O(n ^ 2)
# Time: O(log(n) * n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        # dijkstra 
        
        heap = [(grid[0][0], 0, 0)]
        
        while heap:
            
            t, r, c = heappop(heap)

            if (r, c) == (n-1, n-1): return t
            
            if grid[r][c] == -1: continue # already found (r, c) with smaller time
                
            grid[r][c] = -1 # mark as visited
            
            for dxn in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dxn[0], c + dxn[1]
                if (0 <= nr < n and 0 <= nc < n) and grid[nr][nc] != -1:
                    nt = max(t, grid[nr][nc]) # new time
                    heappush(heap, (nt, nr, nc))