# link - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        ans = 0

        while (start < end):
            ans = max(ans, (end - start) * min(height[start], height[end]))

            if height[start] <= height[end]:
                while (height[start] <= height[end] and start < end):
                    start += 1
                    ans = max(ans, (end - start) * min(height[start], height[end]))
            else:
                while (height[end] < height[start] and start < end):
                    end -= 1
                    ans = max(ans, (end - start) * min(height[start], height[end]))

        return ans
