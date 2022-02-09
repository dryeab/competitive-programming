# link - https://leetcode.com/problems/k-diff-pairs-in-an-array/

# space: O(n)
# time: O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans, count = 0, Counter(nums)
        for i in count:
            if k == 0:
                ans += 1 if count[i] > 1 else 0
            else:
                ans += min(count[i+k], 1)
        return ans
