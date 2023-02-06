class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        
        dp = Counter()
        for word in words:
            dp[word] = max(dp[word[:i] + word[i+1:]] for i in range(len(word))) + 1
        
        return max(dp.values())