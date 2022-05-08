
# link - https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# space: O(n)
# time: O(n)

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return nums
