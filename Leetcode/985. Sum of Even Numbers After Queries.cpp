/**
 * https://leetcode.com/problems/sum-of-even-numbers-after-queries/
 * Time: O(N + M)
 * Space: O(N)
 */

class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int> &nums, vector<vector<int>> &queries) {

        int sum = 0;
        for (int num : nums)
            if (!(num & 1))
                sum += num;

        vector<int> answer;
        for (auto query : queries) {

            int val = query[0], idx = query[1];

            if (!(nums[idx] & 1))
                sum -= nums[idx];

            nums[idx] += val;

            if (!(nums[idx] & 1))
                sum += nums[idx];

            answer.push_back(sum);
        }

        return answer;
    }
};