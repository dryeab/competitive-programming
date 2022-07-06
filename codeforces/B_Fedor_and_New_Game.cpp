/**
 * https://codeforces.com/problemset/problem/467/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    int n, k, m;
    cin >> n >> m >> k;

    vector<int> x(m + 2);

    for (int i = 1; i <= m + 1; ++i)
        cin >> x[i];

    int res = 0, xr, d;
    for (int i = 1; i < m + 1; ++i) {
        xr = x[i] ^ x[m + 1], d = 0;
        while (xr) {
            d += xr & 1;
            xr >>= 1;
        }
        res += d <= k;
    }

    cout << res << endl;
}