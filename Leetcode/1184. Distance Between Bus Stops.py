# link - https://leetcode.com/problems/distance-between-bus-stops/

# space: O(1)
# time: O(n)

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        clockwise = anticlockwise = 0
        
        temp = start
        while (temp != destination):
            clockwise += distance[temp]
            temp = (temp + 1) % len(distance)
            
        temp = start
        while (temp != destination and anticlockwise <= clockwise):
            temp = (temp - 1) % len(distance)
            anticlockwise += distance[temp]
        
        return min(clockwise, anticlockwise)
            
        
