
# link - https://leetcode.com/problems/squares-of-a-sorted-array/

# space - O(1)
# time - O(nlog(n))

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))
        
        for i, val in enumerate(nums):
            nums[i] = val ** 2
        
        return nums
