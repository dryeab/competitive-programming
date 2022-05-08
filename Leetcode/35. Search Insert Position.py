
# Link - https://leetcode.com/problems/search-insert-position/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            mid = (left + right)//2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
                
        return left if target <= nums[-1] else len(nums)
            
