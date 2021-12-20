

# link - https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        c = {}
        for i, value in enumerate(position):
            c[value] = speed[i]

        position.sort(reverse=True)

        min = (target - position[0]) / c[position[0]]
        counter = 1
        for j in range(1, len(position)):
            current = (target - position[j]) / c[position[j]]
            
            if current > min:
                counter += 1
                min = current
                
        return counter
