
# Link - https://leetcode.com/problems/house-robber/

# Space: O(n)
# Time: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        M, dp = 0, [0] * len(nums)
        
        for i in range(len(nums)):
            
            M = max(M, dp[i-2]) if i - 2 >= 0 else 0
            
            dp[i] = M + nums[i]
        
        return max(dp)