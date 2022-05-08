

# Link - https://leetcode.com/problems/maximum-subarray/

# Solution 1 - Kadane
    # Space: O(1)
    # Time: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum_so_far = 0
        start = end = 0

        ans = float('-inf')

        while (end < len(nums)):
            sum_so_far += nums[end]

            ans = max(sum_so_far, ans)

            if sum_so_far < 0:
                start += 1
                start = end + 1
                sum_so_far = 0
            
            end += 1
        
        return ans

# Solution 2 - DP
    # Space: O(1)
    # Time: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = nums[0]
        M = dp
        
        for i in range(1, len(nums)):
            dp = nums[i] + (dp if dp > 0 else 0)
            M = max(M, dp)
        
        return M
