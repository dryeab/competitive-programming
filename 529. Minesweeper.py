class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m, n = len(board), len(board[0])
        
        DIR = [
            (-1, -1), (-1, 0), (-1, 1),      # top
            (0, -1), (0, 1),                 # middle
            (1, -1), (1, 0), (1, 1)          # bottom
        ]
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def hasAdjacentMines(r, c): # returns number of adjacent mines
            ans = 0
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                if inBound(nr, nc) and board[nr][nc] == 'M':
                    ans += 1
            return ans
        
        def reveal(r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                adjMines = hasAdjacentMines(r, c)
                if adjMines:
                    board[r][c] = str(adjMines)
                else:
                    board[r][c] = 'B'
                    for d in DIR:
                        nr, nc = r + d[0], c + d[1]
                        if inBound(nr, nc) and board[nr][nc] in ['M', 'E']:
                            reveal(nr, nc)
        
        reveal(*click)
        
        return board