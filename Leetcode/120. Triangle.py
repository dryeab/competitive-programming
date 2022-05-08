

# Link - https://leetcode.com/problems/triangle/

# Space: O(1)
# Time: O(n^2) :-> n = len(triangle)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
         
            for i in range(1, len(triangle)):
                for j in range(len(triangle[i])):
                    triangle[i][j] += min(
                             triangle[i-1][j-1] if j else float('inf'),
                             triangle[i-1][j] if j < len(triangle[i-1]) else float('inf')
                    )
            
            return min(triangle[-1])