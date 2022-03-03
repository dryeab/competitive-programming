
# Link - https://leetcode.com/problems/find-peak-element/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def findNext(mid):
            if mid + 1 == len(nums):
                return float('-inf')
            return nums[mid + 1]
            
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if findNext(mid) > nums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return left