
# link - https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# space: O(n)
# time: O(nlog(n))

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        i = j = -1
        
        for k in range(len(nums)):
            if nums[k] != sorted_nums[k]:
                if i == -1:
                    i = k
                j = k
                
        return j - i + 1 if i != -1 else 0
