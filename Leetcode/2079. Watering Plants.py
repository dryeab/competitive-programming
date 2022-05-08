
# Link - https://leetcode.com/problems/watering-plants/

# Space: O(1)
# Time: O(n)

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        ans, water_left = 0, capacity
        
        for i in range(len(plants)):
            
            if plants[i] > water_left:
                
                ans += 2*i
                water_left = capacity
                
            ans += 1
            water_left -= plants[i]
        
        return ans