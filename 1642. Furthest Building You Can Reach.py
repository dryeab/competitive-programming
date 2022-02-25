
# Link - https://leetcode.com/problems/furthest-building-you-can-reach/

# Space: O(ladders)
# Time: O(n*log(ladders))

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = [] # min-heap
        
        for i in range(1, len(heights)):
            dif = heights[i] - heights[i-1]
            if dif > 0:
                heapq.heappush(heap, dif)
                while len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i - 1
        return i
