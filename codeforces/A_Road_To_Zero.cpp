/*
    https://codeforces.com/problemset/problem/1342/A
    Time: O(1)
    Space: O(1)
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        long long x, y, a, b;
        cin >> x >> y;
        cin >> a >> b;

        if (x > y)
            swap(x, y);

        long long ans = (y - x) * a;
        ans += min(2 * x * a, x * b);

        cout << ans << endl;
    }
}