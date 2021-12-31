
# link - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return pow(1/x, -n)
        if n % 2 == 0:
            return  pow(x, n//2) ** 2
        return x * pow(x, n-1)
        
        
