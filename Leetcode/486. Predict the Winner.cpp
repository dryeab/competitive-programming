/**
 * https://leetcode.com/problems/predict-the-winner/
 * Time: O(N^2)
 * Space: O(N)
 */

class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        
        int n = nums.size();
        vector<int> dp(n);
        
        for (int i = n - 1; i >= 0; --i){
            for (int j = i; j < n; ++j){
                if (i == j)
                    dp[j] = nums[i];
                else
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1]);
            }
        }
        
        return dp[n - 1] >= 0;
    }
};