/**
 * https://codeforces.com/problemset/problem/550/B
 * Time: O(2 ^ n)
 * O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, l, r, x;
    cin >> n >> l >> r >> x;

    vector<int> c(n);
    for (int &x : c)
        cin >> x;

    int res = 0;
    for (int i = 3; i < (1 << n); ++i) {
        int total = 0, mx = 0, mn = 1e7, cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j)) {
                cnt++;
                total += c[j];
                mx = max(mx, c[j]);
                mn = min(mn, c[j]);
            }
        }

        if (cnt >= 2 && total >= l && total <= r && mx - mn >= x) {
            res++;
        }
    }

    cout << res;
}