
# Link - https://leetcode.com/problems/get-maximum-in-generated-array/

# Space: O(n)
# Time: O(n)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n < 2: return n
        
        dp = [0]*(n+1)
        dp[0], dp[1] = [0, 1]
        
        M = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i//2] + (0 if i%2==0 else dp[i//2+1])
            M = max(M, dp[i])
        
        return M