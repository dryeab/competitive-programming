
# Link - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        parent = {(i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"}
        size = {(i, j): 1 for i in range(m) for j in range(n) if grid[i][j] == "1"}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2 = find(v1), find(v2)
            
            if root1 != root2:
                
                if size[root1] < size[root2]:
                    parent[root1] = root2
                    size[root2] += size[root1]
                else:
                    parent[root2] = root1
                    size[root1] += size[root2]
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        DIR = [(-1, 0), (0, -1)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    for d in DIR:
                        nr, nc = r + d[0], c + d[1]
                        if inBound(nr, nc) and grid[nr][nc] == "1":
                            union((nr, nc), (r, c))
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    find((r, c))

        return len(set(parent.values()))