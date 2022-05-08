
# link - https://leetcode.com/problems/maximum-number-of-coins-you-can-get

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        
        i , n = 0, len(piles)
        ans = 0

        while (i < (n/3)):
            ans += piles[-2 - (2*i)]
            i += 1
        
        return ans
