# link - https://leetcode.com/problems/rearrange-array-elements-by-sign/

# space: O(n)
# time: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, ans = 0, 1, [None] * len(nums)
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        return ans
