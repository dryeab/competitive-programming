
# link - https://leetcode.com/problems/minimum-path-sum/

# space: O(m*n)
# time: O(m*n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid) - 1, len(grid[0]) - 1
        memo = {(m, n): grid[m][n]}
        
        def helper(grid, i, j):
            if i > m or j > n:
                return float('inf')
            if (i, j) not in memo:
                ans = min(helper(grid, i, j+1), helper(grid, i+1, j))
                memo[(i, j)] = grid[i][j] + ans
                
            return memo[(i,j)]
        
        return helper(grid, 0, 0)
