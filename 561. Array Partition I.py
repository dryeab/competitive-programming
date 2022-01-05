# link - https://leetcode.com/problems/array-partition-i/

# space: O(1)
# time: O(nlog(n))

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
            
