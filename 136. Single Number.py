# link - https://leetcode.com/problems/single-number/

# space: O(n)
# time: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for num in c:
            if c[num] % 2: return num
