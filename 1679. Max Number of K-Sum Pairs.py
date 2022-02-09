# link - https://leetcode.com/problems/max-number-of-k-sum-pairs

# space: O(n)
# time: O(n)

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        ans, count = 0, Counter(nums)
        for num in count:
            ans += min(count[num], count[k-num])
        return ans//2
