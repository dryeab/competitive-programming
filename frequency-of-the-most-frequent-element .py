
# link - https://leetcode.com/problems/frequency-of-the-most-frequent-element

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        nums.sort(reverse=True)

        start = end = 0
        ans = 1

        while (end < len(nums)):
            if (nums[start] - nums[end]) > k:
                ans = max(ans, end-start)
                k += (end-start-1)*(nums[start] - nums[start+1])
                start += 1
            else:
                k -= nums[start] - nums[end]
                end += 1

        ans = max(ans, end-start)
        return ans
