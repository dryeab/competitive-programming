
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

# Solution 2
  # Space: O(1)
  # Time: O(m*log(n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search
        def search(arr, target):
            
            left, right = 0, len(arr) - 1
            
            while left <= right:
                
                mid = (left + right)//2
                
                if arr[mid] == target:
                    return True
                
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return False
        
        for row in matrix:
            if search(row, target):
                return True
            
        return False
