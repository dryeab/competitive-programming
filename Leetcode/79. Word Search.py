
# Link - https://leetcode.com/problems/word-search/

# Space: O(n)
# Time: ~

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        visited = set()
        DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        def helper(r, c, i):

            if i == len(word) - 1: # reached at the end
                return True
            
            for d in DIR:
                nr, nc = r + d[0], c + d[1] # new row, col
                if inBound(nr, nc) and (nr, nc) not in visited and board[nr][nc] == word[i+1]:
                    visited.add((nr, nc))
                    if helper(nr, nc, i+1):
                        return True
                    visited.remove((nr, nc))
            
            return False
        
        for r in range(m):
            for c in range(n):
                visited.add((r, c))
                if board[r][c] == word[0] and helper(r, c, 0):
                    return True
                visited.remove((r, c))
        
        return False