
# Link - https://leetcode.com/problems/number-of-enclaves/

# Space: O(m * n)
# Time: O(m * n)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def dfs(r, c):
            if not inBound(r, c) or grid[r][c] != 1:
                return 
            grid[r][c] = -1 # mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        #### Mark regions that can go out ###
        
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
            
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)
            
        ######################
        
        return sum(row.count(1) for row in grid)