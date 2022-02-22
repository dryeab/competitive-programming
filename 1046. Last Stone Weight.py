
# link - https://leetcode.com/problems/last-stone-weight/

# space: O(1)
# time: O(nlog(n))

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, -abs(x-y))
                
        return -stones[0] if stones else 0
