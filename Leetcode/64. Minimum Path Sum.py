
# Link - https://leetcode.com/problems/minimum-path-sum/

# Space: O(m*n)
# Time: O(m*n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i or j: # not [0][0]
                    dp[i][j] = grid[i][j] + \
                        min(dp[i-1][j] if i else float('inf'), dp[i][j-1] if j else float('inf'))
        
        return dp[-1][-1]