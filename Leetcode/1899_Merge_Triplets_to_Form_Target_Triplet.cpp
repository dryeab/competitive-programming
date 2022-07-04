/*
    https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
    Time: O(n)
    Space: O(1)
*/

class Solution
{
public:
    bool mergeTriplets(vector<vector<int>> &triplets, vector<int> &target)
    {
        int tx = target[0], ty = target[1], tz = target[2];
        bool res[] = {false, false, false};

        for (auto triplet : triplets)
        {
            int x = triplet[0], y = triplet[1], z = triplet[2];
            if (x > tx || y > ty || z > tz)
                continue;
            if (x == tx)
                res[0] = true;
            if (y == ty)
                res[1] = true;
            if (z == tz)
                res[2] = true;
        }

        return res[0] && res[1] && res[2];
    }
};