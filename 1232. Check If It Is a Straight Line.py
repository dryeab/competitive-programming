
# Link - https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Space: O(1)
# Time: O(n)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        def findSlope(point1, point2):
            if point1[0] == point2[0]:
                return float('inf')
            return (point1[1] - point2[1]) / (point1[0] - point2[0])
        
        slope = findSlope(coordinates[0], coordinates[1])
        
        for i in range(1, len(coordinates)-1):
            
            if findSlope(coordinates[i], coordinates[i+1]) != slope:
                return False
        
        return True
                