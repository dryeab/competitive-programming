
# Link - https://leetcode.com/problems/sum-of-subarray-ranges/

# Space: O(1)
# Time: O(n)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i in range(len(nums)):
            
            m = M = nums[i] # min, max
            
            for j in range(i+1, len(nums)):
                
                m = min(m, nums[j])
                M = max(M, nums[j])
                ans += M - m

        return ans