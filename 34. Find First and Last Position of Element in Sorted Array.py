# Link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = [-1, -1]
        
        if not len(nums): return ans
        
        #### left index #######
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] != target: return ans
        
        ans[0] = left
        
        #### right index ####
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] != target:
            left -= 1
        
        ans[1] = left
        
        return ans