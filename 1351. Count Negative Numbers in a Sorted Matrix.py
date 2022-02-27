# Link - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Solution 1
  # Space: O(1)
  # Time: O(m + n)
  
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = col = 0
        for row in range(len(grid)-1, -1, -1):
            while col < len(grid[0]) and grid[row][col] >= 0:
                col += 1
            ans += len(grid[0]) - col
        return ans


# Solution 2
  # Space: O(1)
  # Time: O(m*log(n))
  
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for row in grid:
            
            i, j = 0, len(row) - 1
            
            while i < j:
                
                mid = (i+j)//2
                
                if row[mid] < 0:
                    j = mid
                else: 
                    i = mid + 1
                    
            if row[i] < 0:
                ans += len(row) - i
            
        return ans
