
# Link - https://leetcode.com/problems/decode-ways/

# Space: O(n)
# Time: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0]*len(s)
        dp[0] = (s[0] != '0') + 0
        
        for i in range(1, len(s)):
            
            if dp[i-1] == 0:
                return 0
            
            if s[i] != '0':
                dp[i] += dp[i-1]
                
            if '10' <= s[i-1] + s[i] <= '26':
                dp[i] += dp[i-2] if i > 1 else 1
        
        return dp[-1]