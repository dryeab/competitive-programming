
# Link - https://leetcode.com/problems/search-a-2d-matrix/

# Solution 1
  # Space: O(1)
  # Time: O(m*n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False
