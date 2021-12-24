
# link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = start = 0
        for end in range(len(prices)):
            if prices[end] < prices[start]:
                start = end
            ans = max(prices[end] - prices[start], ans)
        return ans
