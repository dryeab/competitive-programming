/*
    https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
    Time: O(nlog(n) + mlog(m))
    Space: O(1)
*/

class Solution
{
public:
    int maxArea(int h, int w, vector<int> &horizontalCuts, vector<int> &verticalCuts)
    {
        horizontalCuts.push_back(h);
        verticalCuts.push_back(w);

        const int mod = 1e9 + 7, n = horizontalCuts.size(), m = verticalCuts.size();

        sort(horizontalCuts.begin(), horizontalCuts.end());
        sort(verticalCuts.begin(), verticalCuts.end());

        int y = horizontalCuts[0];
        for (int i = 1; i < n; ++i)
            y = max(y, horizontalCuts[i] - horizontalCuts[i - 1]);

        int x = verticalCuts[0];
        for (int i = 1; i < m; ++i)
            x = max(x, verticalCuts[i] - verticalCuts[i - 1]);

        return (1ll * (x % mod) * (y % mod)) % mod;
    }
};