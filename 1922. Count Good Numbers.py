
# link - https://leetcode.com/problems/count-good-numbers/

# space: O(1) : excluding the stacks space
# time: O(log(n))

# math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        m = 10**9 + 7

        return pow(20, (n//2), m) * (5*(n%2) if n%2 else 1) % m
    
    
# recursive solution    
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        m = 10**9 + 7
        
        if n == 1:
            result =  5
        elif n % 2 == 0:
            half = self.countGoodNumbers(n//2)
            if n % 4 == 0:
                result = (half * half)
            else:
                result = pow(20, n//2, m)
        else:
            result =  5 * self.countGoodNumbers(n-1)
        return result % m
