/**
 * https://leetcode.com/problems/interleaving-string/
 * Time: O(mn)
 * Space: O(m)
 */

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        
        int n = s1.size(), m = s2.size();
        
        if (s3.size() != n + m)
            return false;
        
        vector<int> dp(m+1);
        
        for (int i = 0; i <= n; ++i){
            for (int j = 0; j <= m; ++j){
                if (i == 0 && j == 0)
                    dp[0] = 1;
                else if (i == 0){
                    dp[j] = dp[j-1] && (s3[i+j-1] == s2[j-1]);
                } else if (j == 0){
                    dp[j] = dp[j] && (s3[i+j-1] == s1[i-1]);
                } else {
                    dp[j] = (dp[j] && s3[i+j-1] == s1[i-1]) || (dp[j-1] && (s3[i+j-1] == s2[j-1]));
                }
            }
        }
        
        return dp[m];
    }
};