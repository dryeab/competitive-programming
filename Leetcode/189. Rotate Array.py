# link - https://leetcode.com/problems/rotate-array/

# space: O(1)
# time: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k %= len(nums)
        
        if k:
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
