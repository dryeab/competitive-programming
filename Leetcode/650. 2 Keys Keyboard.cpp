/**
 * https://leetcode.com/problems/2-keys-keyboard/
 * Time: O(N^2)
 * Space: O(N)
 */

class Solution {
public:
    int minSteps(int n) {
     
        vector<int> dp(n + 1);
        
        for (int i = 2; i <= n; ++i){
            for (int j = i - 1; j > 0; --j)
                if (i % j == 0){
                    dp[i] = dp[j] + (i / j);
                    break;
                }
        }
        
        return dp[n];
    }
};