
# Link - https://leetcode.com/problems/valid-perfect-square/

# Space: O(1)
# Time: O(n)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left , right = 1, num
        while left < right:
            
            mid = (left + right) // 2
            if mid ** 2 >= num:
                right = mid
            else:
                left = mid + 1
        
        return left**2 == num