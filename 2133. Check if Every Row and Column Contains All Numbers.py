
# Link - https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

# Space: O(n)
# Time: O(n^2)

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n, row, col = len(matrix), defaultdict(set), defaultdict(set)
        
        for i in range(n):
            for j in range(n):
              
                num = matrix[i][j] 
                if num in row[i] or num in col[j]:
                    return False
                
                row[i].add(num)
                col[j].add(num)
        
        return True