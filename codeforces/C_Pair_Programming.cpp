/**
 * https://codeforces.com/contest/1547/problem/C
 * Time: O(n + m)
 * Space: O(n + m)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    int k, n, m;
    cin >> k >> n >> m;

    vector<int> a(n), b(m), res(n + m);
    for (int &x : a)
        cin >> x;
    for (int &x : b)
        cin >> x;

    int i = 0, j = 0;
    for (int l = 0; l < n + m; ++l) {
        if (i < n && (j >= m || a[i] <= b[j]))
            res[l] = a[i++];
        else
            res[l] = b[j++];
        if (res[l] && res[l] > k) {
            cout << -1 << '\n';
            return;
        }
        k += res[l] == 0;
    }

    for (int x : res)
        cout << x << ' ';

    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        // cout << "ans ";
        solve();
    }
}