# link - https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# space: O(1)
# time: O(n)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        first, second = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[second] or first == second:
                second = i
                if nums[second] > nums[first]:
                    first, second = second, first
        return first if nums[first] >= 2*nums[second] else -1
