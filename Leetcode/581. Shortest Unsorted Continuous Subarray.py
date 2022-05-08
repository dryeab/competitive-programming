
# Link - https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Time: O(n)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int: # Space: O(1)
        
        n = len(nums)
        l = r = n
        
        max_so_far, min_so_far = float('-inf'), float('inf')
        
        for i in range(n):
            
            if max_so_far > nums[i]: r = i
            if min_so_far < nums[n - (i + 1)]: l = n - (i + 1)
            
            max_so_far = max(max_so_far, nums[i])
            min_so_far = min(min_so_far, nums[n - (i + 1)])
        
        return r - l + 1 if l != r else 0

# Monotonic Stack
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int: # Space: O(n)
        
        n, max_so_far = len(nums), float('-inf')
        mono_stack = []
        l = r = n
        
        for i in range(n):

            if max_so_far > nums[i]: r = i

            while mono_stack and nums[mono_stack[-1]] > nums[i]:
                l = min(l, mono_stack.pop())
                
            mono_stack.append(i)
            max_so_far = max(max_so_far, nums[i])
        
        return r - l + 1 if r != n else 0