
# link - https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        left = {}
        right = {}

        stack = [] # monotic stack

        for i in range(len(heights)):
            while len(stack) and heights[stack[-1]] > heights[i]:
                left[stack.pop()] = i
            stack.append(i)
            left[i] = len(heights)

        stack = []

        for i in range(len(heights)-1, -1, -1):
            while len(stack) and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            stack.append(i)
            right[i] = -1

        ans = float('-inf')

        for i in left:
            ans = max(ans, heights[i]*(left[i]-right[i]-1))

        return ans
