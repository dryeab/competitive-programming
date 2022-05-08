
# Link - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

# Space: O(1)
# Time: O(n)

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        for i, point in enumerate(points):
            points[i] = point[0]
        points.sort()
        
        ans = 0
        for i in range(1, len(points)):
            ans = max(ans, points[i] - points[i-1])
        
        return ans