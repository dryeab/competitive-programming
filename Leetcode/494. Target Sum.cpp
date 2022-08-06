/**
 * https://leetcode.com/problems/target-sum/
 * Time: O(N * T)
 * Space: O(N * T)
 */

class Solution {
public:
    int n;
    map<pair<int, int>, int> memo;

    int findTargetSumWays(vector<int> &nums, int target) {

        n = nums.size();

        return dp(0, 0, target, nums);
    }

    int dp(int i, int s, int target, vector<int> &nums) {

        if (i == n)
            return s == target;

        if (memo.count({i, s}))
            return memo[{i, s}];

        memo[{i, s}] = dp(i + 1, s + nums[i], target, nums) + dp(i + 1, s - nums[i], target, nums);

        return memo[{i, s}];
    }
};