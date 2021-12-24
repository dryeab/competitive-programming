

# link - https://leetcode.com/problems/maximum-subarray/

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
