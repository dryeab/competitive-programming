# link - https://leetcode.com/problems/house-robber/

# space: O(n)
# time: O(n**2)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def helper(nums, i):
            if i not in memo:
                
                ans = 0
                for j in range(i+2 if i != -1 else 0 , len(nums)):
                    ans = max(ans, helper(nums, j))
                    
                memo[i] = nums[i] + ans if i != -1 else ans
                
            return memo[i]
        
        return helper(nums, -1)
