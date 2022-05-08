class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def find_distance(point):
            import math
            [x, y] = point
            return math.sqrt(x**2 + y**2)
        
        y = sorted(points, key=find_distance)
        
        return y[:k]
