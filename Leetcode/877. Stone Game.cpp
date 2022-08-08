/**
 * https://leetcode.com/problems/stone-game/
 * Time: O(1)
 * Space: O(1)
 */

class Solution {
public:
    bool stoneGame(vector<int> &piles) {

        return true;

        // int n = piles.size();
        // vector<int> dp(n);

        // for (int i = n - 1; i >= 0; --i) {
        //     for (int j = i; j < n; ++j) {
        //         if (i == j)
        //             dp[j] = piles[i];
        //         else
        //             dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1]);
        //     }
        // }

        // return dp[n - 1] > 0;
    }
};