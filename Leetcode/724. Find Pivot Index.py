
# link - https://leetcode.com/problems/find-pivot-index/

# space: O(n)
# time: O(n)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ps = [None] * len(nums)
        
        i, sum = len(nums) - 1, 0
        while (i >= 0):
            ps[i] = sum
            sum += nums[i]
            i -= 1
        
        sum = 0
        for i in range(len(nums)):
            if ps[i] == sum:
                return i
            sum += nums[i]
        
        return -1
