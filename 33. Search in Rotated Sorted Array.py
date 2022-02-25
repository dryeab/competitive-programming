
# Link - https://leetcode.com/problems/search-in-rotated-sorted-array/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findPivot(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right)//2
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        if nums[0] < nums[-1]:
            left, right = 0, len(nums) - 1
        else:
            pivot = findPivot(nums)
            # print(pivot)
            if nums[-1] >= target:
                left, right = pivot, len(nums) - 1
            else:
                left, right = 0, pivot - 1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target: return mid
            if nums[mid] > target: right = mid - 1
            else: left = mid + 1
        return -1
