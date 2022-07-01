/*
    https://codeforces.com/problemset/problem/1374/C
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
        int n;
        cin >> n;

        string s;
        cin >> s;

        int ans = 0, ps = 0;
        for (auto c : s)
        {
            if (c == '(')
                ps++;
            else
                ps--;

            if (ps < 0)
            {
                ans++;
                ps = 0;
            }
        }

        cout << ans << endl;
    }
}