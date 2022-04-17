class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        answer, visited = 0, set()
        
        # (row, col) :-> (left, right, top, bottom)
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        
        def calculateArea(r, c):
            
            visited.add((r,c)) # mark as visited
            
            area = 1
            
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if (inBound(nr, nc)) and (grid[nr][nc] == 1) and ((nr, nc) not in visited):
                    area += calculateArea(nr, nc)
                    
            return area
                          
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    answer = max(answer, calculateArea(r, c))
        
        return answer


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