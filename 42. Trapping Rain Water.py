
# link - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        def find_hills(height):
            hills = []

            for i in range(len(height)):
                if i == 0:
                    if height[1] < height[0]:
                        hills.append(i)
                elif i == len(height)-1:
                    if height[i] > height[i-1]:
                        hills.append(i)
                elif \
                       (height[i-1] < height[i] and height[i+1] < height[i]) \
                    or (height[i-1] == height[i] and height[i+1] < height[i]) \
                    or (height[i+1] == height[i] and height[i-1] < height[i]):
                    hills.append(i)

            return hills

        stack = [] 
        store = {}

        for i in range(len(height)):
            while len(stack) and height[stack[-1]] < height[i]:
                store[stack.pop()] = i
            stack.append(i)
            store[i] = -1

        hills = find_hills(height)

        if len(hills) == 0: return 0

        volume = 0
        start = hills[0]

        for end in hills:
            if store[end] == -1 or height[end] > height[start]:
                min_hill = min(height[start], height[end])

                while (start < end):
                    temp = min_hill - height[start] 
                    volume += temp if temp > 0 else 0
                    start += 1
        
        return volume
