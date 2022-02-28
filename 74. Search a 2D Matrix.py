
# Link - https://leetcode.com/problems/search-a-2d-matrix/

# Solution 1
  # Space: O(1)
  # Time: O(log(mn))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def rowCol(n):
            return n//len(matrix[0]), n%len(matrix[0])
        
        left, right = 0, len(matrix)*len(matrix[0]) - 1
        
        while left < right:
            
            mid = (left + right)//2
            row, col = rowCol(mid)
            
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1
        
        row, col = rowCol(right)
        
        return matrix[row][col] == target