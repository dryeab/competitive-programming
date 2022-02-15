
# link - https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

# space: O(1)
# time: O(n)

class Solution:
    def countElements(self, nums: List[int]) -> int:
        return max(0, len(nums) - (nums.count(min(nums)) + nums.count(max(nums))))
