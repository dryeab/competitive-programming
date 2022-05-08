
# Link - https://leetcode.com/problems/word-break/

# Space: O(n + m) :-> n = len(s), len(wordDict)
# Time: O(n^2)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict, dp = set(wordDict), [False] * len(s)
        
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j] and s[j+1:i+1] in wordDict:
                        dp[i] = True
                        break
                        
        return dp[-1]