
# link - https://leetcode.com/problems/keep-multiplying-found-values-by-two/

# space: O(n)
# time: O(n)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
