# link - https://leetcode.com/problems/move-zeroes/

# space: O(1)
# time: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j]: 
                nums[i] = nums[j]
                if i < j:
                    nums[j] = 0
                i += 1
