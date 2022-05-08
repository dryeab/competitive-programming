
# Link - https://leetcode.com/problems/last-stone-weight/

# Space: O(n)
# Time: O(n*log(n))

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            
            x, y = [heapq.heappop(stones) for _ in range(2)]
            
            if x != y:
                heapq.heappush(stones, -abs(x-y))
                
        return -stones[0] if stones else 0
