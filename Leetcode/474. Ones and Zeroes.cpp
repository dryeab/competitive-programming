/**
 * https://leetcode.com/problems/ones-and-zeroes/
 * Time: O(L * M * N)
 * Space: O(M * N)
 */

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        
        auto dp = vector<vector<int>>(m + 1, vector<int>(n + 1));
        
        for (auto str: strs){
            
            int zero = count(str.begin(), str.end(), '0');
            int one = count(str.begin(), str.end(), '1');
            
            for (int i = m; i >= zero; --i){
                for (int j = n; j >= one; --j){
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one]);
                }
            }
            
        }
        
        return dp[m][n];
    }
};