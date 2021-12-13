# link - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/submissions/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        result = [None] * len(nums)

        i = j = 0
        while (j < len(nums)):
            result[i] = nums[j]
            j += 1
            i += 2
            if i >= len(nums):
                i = 1
        return result
