/**
 * https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
 * Time: O(NlogN)
 * Space: O(N)
 */

class Solution {
public:
    int minimumMountainRemovals(vector<int> &nums) {

        int n = nums.size();
        vector<int> dp;
        vector<pair<int, int>> res(n);

        for (int i = 0; i < n; ++i) {

            int num = nums[i];
            int j = upper_bound(dp.begin(), dp.end(), num) - dp.begin();

            if (j && dp[j - 1] == num) {
                res[i].first = j;
                continue;
            }

            if (j >= dp.size())
                dp.push_back(num);
            else
                dp[j] = num;

            res[i].first = j + 1;
        }

        dp.clear();

        for (int i = n - 1; i >= 0; --i) {

            int num = nums[i];
            int j = upper_bound(dp.begin(), dp.end(), num) - dp.begin();

            if (j && dp[j - 1] == num) {
                res[i].second = j;
                continue;
            }
            if (j >= dp.size())
                dp.push_back(num);
            else
                dp[j] = num;

            res[i].second = j + 1;
        }

        int ans = 1;
        for (int i = 0; i < n; ++i) {
            // cout << res[i].first << ' ' << res[i].second << endl;
            if (res[i].first > 1 && res[i].second > 1)
                ans = max(ans, res[i].first + res[i].second - 1);
        }

        return n - ans;
    }
};

// class Solution {
// public:
//     int minimumMountainRemovals(vector<int> &nums) {

//         int n = nums.size();
//         vector<int> dp1(n), dp2(n);

//         for (int i = 0; i < n; ++i) {
//             int mn = i;
//             for (int j = 0; j < i; ++j) {
//                 if (nums[j] < nums[i]) {
//                     mn = min(mn, dp1[j] + i - j - 1);
//                 }
//             }
//             dp1[i] = mn;
//         }

//         for (int i = n - 1; i >= 0; --i) {
//             int mn = n - 1 - i;
//             for (int j = i + 1; j < n; ++j) {
//                 if (nums[j] < nums[i]) {
//                     mn = min(mn, dp2[j] + j - i - 1);
//                 }
//             }
//             dp2[i] = mn;
//         }

//         int res = n - 1;
//         for (int i = 1; i < n - 1; ++i) {
//             if (dp1[i] < i && dp2[i] < n - 1 - i)
//                 res = min(res, dp1[i] + dp2[i]);
//         }

//         return res;
//     }
// };