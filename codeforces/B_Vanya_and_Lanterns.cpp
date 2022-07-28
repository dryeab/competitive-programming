/**
 * https://codeforces.com/contest/492/problem/B
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    int n, l;
    cin >> n >> l;

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    sort(a, a + n);

    double res = max(a[0], l - a[n - 1]);

    for (int i = 0; i < n - 1; ++i)
        res = max(res, (a[i + 1] - a[i]) / 2.0);

    cout << fixed << setprecision(9) << res;
}