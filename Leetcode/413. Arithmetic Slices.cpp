/**
 * https://leetcode.com/problems/arithmetic-slices/
 * Time: O(N)
 * Space: O(1)
 */

class Solution {
public:
    int numberOfArithmeticSlices(vector<int> &nums) {

        int n = nums.size(), dp = 0, res = 0;

        for (int i = 2; i < n; ++i) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2])
                dp++;
            else
                dp = 0;
            res += dp;
        }

        return res;
    }
};