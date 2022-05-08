
# Link - https://leetcode.com/problems/arranging-coins/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        start, end = 1, n
        
        while start < end:
            
            mid = start + ((end - start + 1) >> 1);
            val = (mid)*(mid+1)/2
            
            if val > n:
                end = mid - 1
            else:
                start = mid
                
        return start
