
# link - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        m = 10**9 + 7

        return pow(20, (n//2), m) * (5*(n%2) if n%2 else 1) % m
