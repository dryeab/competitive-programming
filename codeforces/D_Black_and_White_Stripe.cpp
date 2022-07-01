/*
    https://codeforces.com/problemset/problem/1690/D
    Time: O(n)
    Space: O(1)
*/

#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, k;
        cin >> n >> k;

        string s;
        cin >> s;

        int ans = 1e9, cur = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == 'W')
                cur++;

            if (i >= k && s[i - k] == 'W')
                cur--;

            if (i >= k - 1 && ans > cur)
                ans = cur;
        }

        cout << ans << endl;
    }
}