
# Link - https://leetcode.com/problems/min-cost-climbing-stairs/

# Space: O(n)
# Time: O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         
        dp = [0]*(len(cost))
        
        for i in range(len(cost)):
            dp[i] = cost[i] + min(dp[i-1] if i - 1 >= 0 else 0, dp[i-2] if i - 2 >= 0 else 0)
        
        return min(dp[-1], dp[-2])