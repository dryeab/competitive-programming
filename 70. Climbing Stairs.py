
# Link - https://leetcode.com/problems/climbing-stairs/

# Space: O(1)
# Time: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1: return n
        
        dp = [1, 1]
        
        for i in range(2, n):
            dp[0], dp[1] = dp[1], sum(dp)
        
        return sum(dp)
