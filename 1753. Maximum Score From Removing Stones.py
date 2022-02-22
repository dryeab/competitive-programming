
# Link - https://leetcode.com/problems/maximum-score-from-removing-stones/

# Space: O(1)
# Time: ~

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        piles = [-a, -b, -c]
        
        heapq.heapify(piles)
        
        ans = 0
        while piles:
            
            x = -heapq.heappop(piles)
            y = -heapq.heappop(piles) if piles else None
            
            x -= 1
            if x:
                heapq.heappush(piles, -x)
            
            if y:
                y -= 1
                if y:
                    heapq.heappush(piles, -y)
                ans += 1
                
        return ans
