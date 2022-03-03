class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n, visited = len(board), len(board[0]), set()
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def markRegion(r, c, marker):
            visited.add((r,c))
            board[r][c] = marker
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and board[nr][nc] == 'O' and (nr, nc) not in visited:
                    markRegion(nr, nc, marker)
        
        # mark the boarders first
        for r in [0, m-1]:
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    markRegion(r, c, 'O')
                    
        for c in [0, n-1]:
            for r in range(m):
                if board[r][c] == 'O' and (r, c) not in visited:
                    markRegion(r, c, 'O')
                    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in visited:
                    markRegion(r, c, 'X')