
# Link - https://leetcode.com/problems/find-the-duplicate-number/

# Space: O(1)
# Time: O(n*log(n))

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        start, end = 1, len(nums) - 1
        
        while start < end:
            
            mid = (start + end)//2
            
            if sum(1 for num in nums if num <= mid) > mid:
                end = mid
            else:
                start = mid + 1
                
        return start