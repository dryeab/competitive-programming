/**
 * https://leetcode.com/problems/house-robber-ii/
 * Time: O(N)
 * Space: O(N)
 */

class Solution {
public:
    map<pair<int, bool>, int> memo;

    int rob(vector<int> &nums) {

        if (nums.size() == 1)
            return nums[0];

        return max(nums[0] + dp(2, false, nums), dp(1, true, nums));
    }

    int dp(int i, bool can, vector<int> &nums) {

        if (i >= nums.size())
            return 0;

        if (i == nums.size() - 1)
            return can ? nums[i] : 0;

        if (memo.count({i, can}))
            return memo[{i, can}];

        memo[{i, can}] = max(nums[i] + dp(i + 2, can, nums), dp(i + 1, can, nums));

        return memo[{i, can}];
    }
};