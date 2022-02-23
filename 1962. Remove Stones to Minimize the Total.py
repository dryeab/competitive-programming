
# Link - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

# Space: O(n)
# Time: O(n*log(n))

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-pile for pile in piles]
        
        heapq.heapify(piles)
        
        for _ in range(k):
            val = ceil((-heapq.heappop(piles))/2)
            if val:
                heapq.heappush(piles, -val)
        
        return -sum(piles)
