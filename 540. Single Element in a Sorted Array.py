
# Link - https://leetcode.com/problems/single-element-in-a-sorted-array/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def l(i):
            return i == 0 or nums[i] != nums[i-1]
        
        def r(i):
            return i == len(nums) -1 or nums[i] != nums[i+1]
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            mid = (left + right)//2
            
            if l(mid) and r(mid):
                return nums[mid]
            
            if not l(mid): # mid is the right
                if mid % 2:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # mid is left
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    right = mid
