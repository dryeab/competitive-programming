
# Link - https://leetcode.com/problems/valid-sudoku/

# Space: 
# Time: 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row, col, group = [defaultdict(set) for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                
                num, g_no =  board[i][j], (i//3)*3 + (j//3)
                
                if num != '.':
                    
                    if num in group[g_no] or num in row[i] or num in col[j]:
                        return False

                    group[g_no].add(num)
                    row[i].add(num)
                    col[j].add(num)
        
        return True