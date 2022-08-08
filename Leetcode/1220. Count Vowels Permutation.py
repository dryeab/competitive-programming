# https://leetcode.com/problems/count-vowels-permutation/
# Time: O(N)
# Space: O(N)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        followers = [
            [1],
            [0, 2],
            [0, 1, 3, 4],
            [2, 4],
            [0]
        ]

        MOD = 10**9 + 7
        dp = [[1] * 5 for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            for j in range(5):
                dp[i][j] = 0
                for follower in followers[j]:
                    dp[i][j] += dp[i + 1][follower]
                    dp[i][j] %=  MOD
        
        return sum(dp[0]) % MOD
