
# Link - https://leetcode.com/problems/integer-break/

# Space: O(n)
# Time: O(n^2)

class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0, 1, 1]  # dp[i] = max product of i
        for i in range(3, n+1):
            dp.append(
                max(
                    max(dp[j]*(i-j), j*(i-j)) for j in range(i)
                )
            )

        return dp[-1]
