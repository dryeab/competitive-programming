
# Link - https://leetcode.com/problems/surrounded-regions/

# Space: O(m * n)
# Time: O(m * n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def dfs(r, c):
            if not inBound(r, c) or board[r][c] != 'O':
                return
            
            board[r][c] = "#"
                
            dfs(r + 1, c) # right
            dfs(r - 1, c) # left
            dfs(r, c + 1) # down
            dfs(r, c - 1) # up
        
        #### Mark the border regions first ####
        
        for r in [0, m-1]:
            for c in range(n):
                dfs(r, c)
                
        for c in [0, n-1]:
            for r in range(m):
                dfs(r, c)
                
        #############################
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == '#': board[r][c] = 'O'