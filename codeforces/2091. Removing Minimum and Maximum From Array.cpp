/*

Link - https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
Time - O(n)
Space - O(1)

*/

class Solution
{
public:
    int minimumDeletions(vector<int> &nums)
    {

        /*

        Three case for i < j

        1, remove from 0 to i and from n to j
        2, remove from 0 to j
        3, remove from n to i

        */

        int n = nums.size(), M = 0, m = 0;

        for (int i = 0; i < n; ++i)
        {
            if (nums[m] > nums[i])
                m = i;
            if (nums[M] < nums[i])
                M = i;
        }

        if (m > M)
            swap(m, M);

        return min({M + 1, n - m, n - (M - m - 1)});
    }
};