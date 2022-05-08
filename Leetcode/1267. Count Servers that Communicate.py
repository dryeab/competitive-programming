
# Link - https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        col, row = defaultdict(int), defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
        
        for i in range(n): # col
            for j in range(m): # row
                col[i] += grid[j][i]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (col[j] > 1 or row[i] > 1):
                    ans += 1
        
        return ans