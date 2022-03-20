
# Link - https://leetcode.com/problems/next-greater-element-ii/

# Space: O(n)
# Time: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        M, ans = max(nums), [-1]*len(nums)
        i, j, stack = 0, 0, []
        
        while i <= len(nums):
            
            if nums[j] == M:
                i += 1
                
            while stack and nums[stack[-1]] < nums[j]:
                ans[stack.pop()] = nums[j]
                i += 1
            
            if nums[j] != M and ans[j] == -1:
                stack.append(j)
            
            j = (j+1)%len(nums)
        
        return ans