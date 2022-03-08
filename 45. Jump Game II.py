
# Link - https://leetcode.com/problems/jump-game-ii/

# Space: O(n)
# Time: O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left, dp = 0, [0]*len(nums)
        
        for i in range(1, len(nums)):
            while i > left + nums[left]:
                left += 1
            dp[i] = dp[left] + 1
        
        return dp[-1]