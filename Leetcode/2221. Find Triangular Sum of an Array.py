
# Link - https://leetcode.com/problems/find-triangular-sum-of-an-array/

# Space: O(1)
# Time: O(n^2)

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()
        
        return nums[0]