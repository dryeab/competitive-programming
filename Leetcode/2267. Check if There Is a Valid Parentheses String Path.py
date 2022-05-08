class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        visited = set()
        
        def dfs(r, c, ops):
            
            if (r, c, ops) in visited or not inBound(r, c): return False
            
            visited.add((r, c, ops))
            
            ops += [1, -1][grid[r][c] == ')']
            
            if ops < 0: return False
            
            if r == m-1 and c == n-1: return ops == 0
            
            return dfs(r + 1, c, ops) or dfs(r, c + 1, ops)
  
        return dfs(0, 0, 0)