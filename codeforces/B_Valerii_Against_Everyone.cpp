/*
    https://codeforces.com/problemset/problem/1438/B
    Time: O(n)
    Space: O(1)
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, x;
    cin >> t;

    while (t--)
    {
        cin >> n;

        set<int> s;
        for (int i = 0; i < n; ++i)
        {
            cin >> x;
            s.insert(x);
        }

        printf(s.size() != n ? "YES\n" : "NO\n");
    }
}