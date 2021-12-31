# link - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        
        store = [None] * (n+1)
        
        def helper(n):
            if n < 2:
                return n
            if store[n]:
                return store[n]
            ans = helper(n-1) + helper(n-2)
            store[n] = ans
            return ans
        
        return helper(n)
