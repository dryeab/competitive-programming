/*

    Link - https://codeforces.com/contest/1696/problem/B
    Time: O(n)
    Space: O(1)

*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
    {
        cin >> x;
    }

    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] != 0)
        {
            ans += i == 0 || a[i - 1] == 0;
        }
    }

    cout << min(ans, 2) << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }
}