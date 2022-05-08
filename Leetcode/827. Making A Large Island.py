
# Link - https://leetcode.com/problems/making-a-large-island/

# Space: O(n^2)
# Time: O(n^2)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        group, area = {}, {}
        
        def dfs(r, c, rep):
            
            group[r, c] = rep
            
            size = 1
            for dxn in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nr, nc = r + dxn[0], c + dxn[1]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in group:
                    size += dfs(nr, nc, rep)
                    
            return size
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] and (r, c) not in group:
                    area[r, c] = dfs(r, c, (r, c))
        
        if not area: return 1
        
        ans = max(area.values())
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    gs = set() # adj groups
                    for dxn in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        nr, nc = r + dxn[0], c + dxn[1]
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            gs.add(group[nr, nc])
                    ans = max(ans, 1 + sum(area[g] for g in gs))
        
        return ans