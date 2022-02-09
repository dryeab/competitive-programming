
# link - https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

# space: O(n)
# time: O(n)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans, count = 0, Counter(nums)
        for num in nums:
            count[num] -= 1
            ans += count[k+num] + count[num-k]
        return ans
