
# Link - https://leetcode.com/problems/jump-game/

# Space: O(1)
# Time: O(n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        M = nums[0] # maximum i you could possibly reach
        for i, num in enumerate(nums):
            if M < i:
                return False
            M = max(M, i + num)
        return True