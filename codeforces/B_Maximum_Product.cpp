/**
 * https://codeforces.com/contest/1406/problem/B
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n;
        cin >> n;

        int a[n];
        for (int i = 0; i < n; ++i)
            cin >> a[i];

        sort(a, a + n);

        ll res = LLONG_MIN;
        for (int i = 0; i <= 5; ++i) {
            ll cur = 1;
            for (int j = 0; j < i; ++j)
                cur *= a[j];
            for (int j = n - 1; j >= n - (5 - i); --j)
                cur *= a[j];
            res = max(res, cur);
        }

        cout << res << '\n';
    }
}