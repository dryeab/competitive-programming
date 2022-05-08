# Link - https://leetcode.com/problems/search-a-2d-matrix-ii/

# Space: O(1)
# time: O(m*log(n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            
            i, j = 0, len(row) - 1
        
            while i <= j:
                mid = (i+j)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
                    
        return False
