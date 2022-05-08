
# Link - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# Space: O(1)
# Time: O(nlog(n))

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        
        ans = i = 0
        while i < len(points):
            
            ans += 1
            
            start, end = -2**31, 2**31
            
            while i < len(points) and points[i][0] in range(start, end):
                start = max(start, points[i][0])
                end = min(end, points[i][1]+1)
                i += 1
        
        return ans