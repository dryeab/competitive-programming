class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        self.exists = False
        
        m, n = len(grid), len(grid[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        visited = set()
        
        right = {1, 4, 6}
        left = {1, 3, 5}
        up = {2, 5, 6}
        down = {2, 3, 4}
        
        def dfs(r, c):
            
            if self.exists or (r, c) in visited: return
            
            visited.add((r, c))
            
            if r == m-1 and c == n-1:
                self.exists = True
                return
            
            if grid[r][c] in right: # right
                if inBound(r, c+1) and grid[r][c+1] in left:
                    dfs(r, c+1)
                
            if grid[r][c] in left: # left
                if inBound(r, c-1) and grid[r][c-1] in right:
                    dfs(r, c-1)
                
                
            if grid[r][c] in up: # up
                if inBound(r-1, c) and grid[r-1][c] in down:
                    dfs(r-1, c)
                
            if grid[r][c] in down: # down
                if inBound(r+1, c) and grid[r+1][c] in up:
                    dfs(r+1, c)
        
        dfs(0, 0)
        
        return self.exists