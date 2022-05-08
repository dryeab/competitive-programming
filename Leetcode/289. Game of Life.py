
# Link - https://leetcode.com/problems/game-of-life/

# Space: O(1)
# Time: O(m * n)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def countAliveNeighbors(r, c):
            count = 0
            for d in DIR:
                nr, nc = r + d[0], c + d[1]
                count += inBound(nr, nc) and board[nr][nc] in [1, -2]
            return count
        
        for r in range(m):
            for c in range(n):
                alive = countAliveNeighbors(r, c)
                if board[r][c]:
                    if alive < 2 or alive > 3:
                        board[r][c] = -2 # dies
                else:
                    if alive == 3:
                        board[r][c] = -1 # borns
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 1
                if board[r][c] == -2:
                    board[r][c] = 0