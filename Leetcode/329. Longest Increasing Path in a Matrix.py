
# Link - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Space: O(m*n)
# Time: O(m*n)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        memo = {}
        
        def dfs(r, c):
            
            if (r, c) in memo: return memo[r, c]
            
            res = 0
            
            for dxn in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dxn[0], c + dxn[1]
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, dfs(nr, nc))
            
            memo[r, c] = res + 1
            
            return memo[r, c]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return max(memo.values())