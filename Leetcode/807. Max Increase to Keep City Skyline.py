
# Link - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

# Space: O(n)
# Time: O(n^2)

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        # keep the max of each row and col
        
        n, ans, col, row = len(grid), 0, {}, {}
        
        for i in range(n): # i can be row or col
            mr = mc = -1
            for j in range(n): # j can be row or col
                mr = max(mr, grid[i][j])
                mc = max(mc, grid[j][i])
            col[i], row[i] = mc, mr
        
        for r in range(n):
            for c in range(n):
                ans += min(col[c], row[r]) - grid[r][c]
        
        return ans