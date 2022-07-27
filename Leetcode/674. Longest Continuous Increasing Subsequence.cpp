/**
 * https://leetcode.com/problems/longest-continuous-increasing-subsequence/
 * Time: O(n)
 * Space: O(1)
 */

class Solution {
public:
    int findLengthOfLCIS(vector<int> &nums) {

        int res = 1, cur = 1, n = nums.size();
        for (int i = 1; i < n; ++i) {
            if (nums[i] <= nums[i - 1]) {
                res = max(res, cur);
                cur = 0;
            }
            cur++;
        }

        return max(res, cur);
    }
};