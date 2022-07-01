/*
    https://codeforces.com/problemset/problem/577/A
    Time: O(n)
    Space: O(1)
*/

#include <iostream>

using namespace std;

int main()
{
    int n, x;
    cin >> n >> x;

    int ans = 0;
    for (int i = 1; i <= n; ++i)
        if (x % i == 0 && x / i <= n)
            ans++;

    cout << ans << endl;
}