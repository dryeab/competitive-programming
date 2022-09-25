/**
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/
 * Time: O(NM)
 * Space: O(M)
 */

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        
        int n = nums1.size(), m = nums2.size(), res = 0;
        vector<int> dp(m);
        
        for (int i = 0; i < n; ++i){
            int prev = 0, cur = 0;
            for (int j = 0; j < m; ++j){
                cur = dp[j];
                if (nums1[i] == nums2[j]){
                    dp[j] = 1 + prev;
                    res = max(res, dp[j]);
                } else
                    dp[j] = 0;
                prev = cur;
            }
        }
        
        return res;
    }
};