# link - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max = float('-inf')
        for i in range(len(nums)):
            x = nums[i] + nums[-(i+1)]
            if max < x:
                max = x
        return max
            
        
