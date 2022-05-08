
# Link - https://leetcode.com/problems/rotting-oranges/

# Space: O(n)
# Time: O(n + m) : n = r * c, m = number of edges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n, q = len(grid), len(grid[0]), deque()
        
        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        if not q: return 0 if fresh_count == 0 else -1
        
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dxn in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dxn[0], c + dxn[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr, nc))
        
        return count - 1 if fresh_count == 0 else -1