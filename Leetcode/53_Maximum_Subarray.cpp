/*
    https://leetcode.com/problems/maximum-subarray/
    Time: O(n)
    Space: O(1)
*/

class Solution
{
    /*
    Kadane's algorithm: don't keep negative subarrays
*/
public:
    int maxSubArray(vector<int> &nums)
    {

        int res = -1e5, sum = 0, i = 0, j = 0;

        while (j < nums.size())
        {

            sum += nums[j];
            res = max(res, sum);

            j++;

            if (sum <= 0)
            {
                i = j;
                sum = 0;
            }
        }

        return res;
    }
};

class Solution
{
    /*
        dp[i] = max of subarray that ends at i
    */
public:
    int maxSubArray(vector<int> &nums)
    {
        int res = nums[0], dp = nums[0];

        for (int i = 1; i < nums.size(); ++i)
        {
            dp = nums[i] + max(dp, 0);
            res = max(res, dp);
        }

        return res;
    }
};