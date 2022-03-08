
# Link - https://leetcode.com/problems/jump-game/

# Space: O(1)
# Time: O(n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = nums[0]
        for i, num in enumerate(nums):
            if dp < i:
                return False
            dp = max(dp, i + num)
        return True