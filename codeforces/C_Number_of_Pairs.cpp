/**
 * https://codeforces.com/problemset/problem/1538/C
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

        int n, l, r;
        cin >> n >> l >> r;

        vector<int> a(n);
        for (int &i : a)
            cin >> i;

        sort(a.begin(), a.end());

        ll res = 0;
        for (int i = 0; i < n; ++i) {
            res += max(0, int(upper_bound(a.begin(), a.end(), r - a[i]) - lower_bound(a.begin(), a.end(), l - a[i])));
            if (l <= a[i] * 2 && a[i] * 2 <= r)
                res--;
        }

        cout << res / 2 << "\n";
    }
}