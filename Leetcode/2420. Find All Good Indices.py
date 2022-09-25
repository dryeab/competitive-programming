
# https://leetcode.com/contest/weekly-contest-312/problems/find-all-good-indices/
# Time: O(N)
# Space: O(N)

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        
        left = [1] * N
        right = [1] * N
        
        for i in range(1, N):
            if nums[i - 1] >= nums[i]:
                left[i] = left[i - 1] + 1
               
        for i in range(N - 2, -1, -1):
            if nums[i + 1] >= nums[i]:
                right[i] = right[i + 1] + 1
        
        res = []
        for i in range(1, N - 1):
            if left[i - 1] >= k and right[i + 1] >= k:
                res.append(i)
        
        return res