# link - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(start, end):
            if start == end:
                return nums[start]

            ans = max(
                nums[start] - helper(start+1, end),
                nums[end] - helper(start, end-1)
            )

            return ans
        return helper(0, len(nums)-1) >= 0
