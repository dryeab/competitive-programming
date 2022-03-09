
# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Space: O(n)
# Time: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # j - index of min(value(i))
        j, dp = 0, [0]*len(prices)
        
        value = lambda i: (dp[i-2] if i > 1 else 0) - prices[i]
        
        for i in range(len(prices)):

            dp[i] = max(
                value(j) + prices[i], # buy at j and sell at i
                (0 if i == 0 else dp[i-1]) # treat i as cooldown
            )
            
            if value(i) > value(j): j = i
        
        return max(dp)

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