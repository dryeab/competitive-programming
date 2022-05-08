
# Link - https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

# Space: O(m)
# Time: O(n*m) :-> m = len(queries), n = len(points)

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        findDistance = lambda x1, y1, x2, y2: sqrt((x1 - x2)**2 + (y1 - y2)**2)
             
        answer = [0]*len(queries)
        for point in points:
            for i, (x, y, r) in enumerate(queries):
                if findDistance(*point, x, y) <= r:
                    answer[i] += 1
        
        return answer