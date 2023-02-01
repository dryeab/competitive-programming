class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(1, m):
                mat[i][j] += mat[i][j - 1]
        
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r1, r2 = max(0, i - k), min(n - 1, i + k)
                c1, c2 = max(0, j - k), min(m - 1, j + k)
                cur = 0
                for r in range(r1, r2 + 1):
                    cur += mat[r][c2] - (mat[r][c1 - 1] if c1 else 0)
                ans[i][j] = cur
        
        return ans