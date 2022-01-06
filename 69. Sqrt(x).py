
# link - https://leetcode.com/problems/sqrtx/

# space: O(1)
# time: o(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, x+1):
            if i * i > x:
                return  i -1
        return x
        
        
        
