/**
 * https://codeforces.com/problemset/problem/1213/B
 * Time: O(n)
 * Space: O(n)
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

        int res = 0, m = INT_MAX;
        for (int i = n - 1; i >= 0; --i) {
            if (m < a[i])
                res++;
            m = min(m, a[i]);
        }

        cout << res << '\n';
    }
}