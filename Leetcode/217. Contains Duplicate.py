# link - https://leetcode.com/problems/contains-duplicate/

# space: O(n)
# time: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in c:
            if c[i] - 1: return True
        return False
