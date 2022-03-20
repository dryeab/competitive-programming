
# Link - https://leetcode.com/problems/unique-paths-iii/

# Space: O(n)
# Time: ~

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inBound = lambda r, c: 0 <= r < len(grid)  and 0 <= c < len(grid[0])
        
        sr = sc = er = ec = count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in [0,1,2]:
                    count += 1
                if grid[i][j] == 1:
                    sr, sc = i, j
                if grid[i][j] == 2:
                    er, ec = i, j
        
        visited = set([(sr, sc)])
        
        def dfs(r, c):
            
            if r == er and c == ec:
                return [0, 1][len(visited) == count]
            
            ans = 0
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and (nr, nc) not in visited and (grid[nr][nc] in [0,2]):
                    visited.add((nr, nc))
                    ans += dfs(nr, nc)
                    visited.remove((nr, nc))
            
            return ans
        
        return dfs(sr, sc)