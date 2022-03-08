
# Link - https://leetcode.com/problems/unique-paths/

# Space: O(m*n)
# Time: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
        
        return dp[-1][-1]
