
# link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# space: O(1)
# time: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, ans = 0, 1, 0
        while (j <= len(prices)):
            if j == len(prices) or prices[j] < prices[j-1]:
                ans += prices[j-1] - prices[i]
                i = j
            j += 1
        return ans
