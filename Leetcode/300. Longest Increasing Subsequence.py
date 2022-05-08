
# Link - https://leetcode.com/problems/longest-increasing-subsequence/

# Space: O(n)
# Time: O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]
        
        for i in range(1, len(nums)):
            M = 0 # max upto i
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    M = max(M, dp[j])
            dp.append(M + 1)
        
        return max(dp)