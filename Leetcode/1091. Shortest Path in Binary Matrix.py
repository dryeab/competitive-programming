
# Link - https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if not (grid[0][0] == grid[n-1][n-1] == 0):
            return -1
        
        q, visited = deque([(0, 0, 1)]), {(0, 0)}
        
        dxn = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while q:
            
            r, c, l = q.popleft()
            
            if r == c == n - 1:
                return l
            
            for dr, dc in dxn:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, l+1))
        
        return -1