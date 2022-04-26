
# Link - https://leetcode.com/problems/max-area-of-island/

# Space: O(m * n)
# Time: O(m * n)

# DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def dfs(r, c):
            
            if not inBound(r, c) or grid[r][c] != 1:
                return 0
              
            grid[r][c] = -1 # mark as visited
            
            return 1 + dfs(r-1, c) + dfs(r, c-1) + dfs(r+1, c) + dfs(r, c+1)
                
        return max(dfs(r, c) for r in range(m) for c in range(n))


# Union Find
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        parent = {(i, j): (i, j) for i in range(m) for j in range(n)}
        size = {(i, j): grid[i][j] for i in range(m) for j in range(n)}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2 = find(v1), find(v2)
            
            if root1 == root2: return
            
            if size[root1] < size[root2]:
                parent[root1] = root2
                size[root2] += size[root1]
            else:
                parent[root2] = root1
                size[root1] += size[root2]
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        DIR = [(0, -1), (-1, 0)] # left, top
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    for d in DIR:
                        nr, nc = r + d[0], c + d[1]
                        if inBound(nr, nc) and grid[nr][nc]:
                            union((r, c), (nr, nc))
        
        return max(size.values())