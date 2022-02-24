# Link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Space: O(1)
# Time: O(log(n))

def search(nums: List[int], target: int, i, j) -> int:

    while i <= j:
        mid = (i+j)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        val = search(nums, target, 0, len(nums)-1)
        
        if val == -1:
            return [-1, -1]
        
        left = right = val
        
        while True:
            val = search(nums, target, 0, left-1)
            if val == -1:
                break;
            left = val
        
        while True:
            val = search(nums, target, right+1, len(nums)-1)
            if val == -1:
                break
            right = val
        
        return [left, right]
