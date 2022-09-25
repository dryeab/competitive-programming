
# https://leetcode.com/contest/weekly-contest-312/problems/longest-subarray-with-maximum-bitwise-and/
# Time: O(N)
# Space: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        mx, res, cur = max(nums), 0, 0
        
        for x in nums:
            if x == mx:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        
        return res