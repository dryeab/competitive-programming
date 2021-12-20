

# link - https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}

        for i in nums2:
            if len(stack) and (stack[-1] < i):
                while (len(stack) and stack[-1] < i):
                    ans[stack.pop()] = i
                stack.append(i)
            else:
                stack.append(i)
        
        while (len(stack)):
            ans[stack.pop()] = -1
        
        for i, j in enumerate(nums1):
            nums1[i] = ans[j]

        return nums1
