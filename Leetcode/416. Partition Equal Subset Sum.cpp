/**
 * https://leetcode.com/problems/partition-equal-subset-sum/
 * Time: O(NS)
 * Space: O(NS)
 */

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        
        int n = nums.size(), sum = accumulate(nums.begin(), nums.end(), 0);
        
        if (sum & 1) return false;
        
        sum >>= 1;
        
        vector<vector<bool>> dp(n + 1, vector<bool>(sum + 1));
        
        for (int i = 0; i <= n; ++i){
            for (int j = 0; j <= sum; ++j){
                if (i == 0 && j == 0)
                    dp[i][j] = true;
                else if (j == 0)
                    dp[i][j] = true;
                else if (i == 0)
                    dp[i][j] = false;
                else{
                    dp[i][j] = dp[i - 1][j];
                    if (nums[i - 1] <= j)
                        dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        
        return dp[n][sum];
    }
};