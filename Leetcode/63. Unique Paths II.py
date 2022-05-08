
# Link - https://leetcode.com/problems/unique-paths-ii/

# Space: O(m*n)
# Time: O(m*n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i or j: # not 0, 0
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)

        return dp[-1][-1]