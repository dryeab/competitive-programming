
# Link - https://leetcode.com/problems/maximum-earnings-from-taxi/

# Space: O(n)
# Time: O(n + m) : m = len(rides)

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        rides.sort()
        
        i, dp = 1, [0] * (n + 1)
        for start, end, tip in rides:
            while start >= i:
                dp[i] = max(dp[i], dp[i-1])
                i += 1
            dp[end] = max(dp[end], dp[start] + end - start + tip)
        
        return max(dp)