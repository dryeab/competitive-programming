
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

      
# Solution 3 (faster than solution 2)
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
        
        
        #### The less than part ####
        left, right = 0, len(matrix) - 1
        while left < right:
            mid = (left + right)//2
            if matrix[mid][0] >= target:
                right = mid
            else:
                left = mid + 1
        range_one = left - 1
        
        
        ##### The greater than part #####
        left, right = 0, len(matrix) - 1
        while left < right:
            mid = (left + right)//2
            # print(left, right, mid)
            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
        range_two = left
    
        # print(range_one, range_two)
        
        for i in range(range_one, range_two+1):
            if search(matrix[i], target):
                return True
        return False
