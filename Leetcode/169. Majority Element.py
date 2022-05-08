
# link - https://leetcode.com/problems/majority-element/

# space: O(1)
# time: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer, count = nums[0], 1
        for i in range(1, len(nums)):
            count += [1, -1][nums[i] != answer]
            if not count:
                answer = nums[i]
                count = 1
        return answer
