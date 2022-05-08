
# Link - https://leetcode.com/problems/koko-eating-bananas/

# Space: O(1)
# Time: O(n*log(M)) : M = max(piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        
        while left < right:
            
            mid = (left + right)//2
            
            if sum(ceil(pile/mid) for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        
        return left