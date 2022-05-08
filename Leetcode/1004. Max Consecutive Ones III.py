
# link - https://leetcode.com/problems/max-consecutive-ones-iii/

# space: O(1)
# time: O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = ans = 0
        while (j < len(nums)):
            k -= (nums[j] == 0)
            if k < 0:
                ans = max(ans, j-i)
                while i <= j and k < 0:
                    k += (nums[i] == 0)
                    i += 1
            j += 1
        return max(ans, j-i)
