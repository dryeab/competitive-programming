
# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Space: O(n)
# Time: O(n^2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0]*len(prices)
        
        for i in range(len(prices)):
            
            M = 0 if i == 0 else dp[i-1] # maximum profit at i by selling at i
            for j in range(i-1, -1, -1):
                profit = prices[i] - prices[j]
                if j > 1:
                    profit += dp[j-2]
                M = max(M, profit)
                
            dp[i] = M
        
        return max(dp)