
# Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
                
        return nums[right]