/**
 * https://codeforces.com/contest/1692/problem/H
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    int n;
    cin >> n;

    vector<int> x(n);
    map<int, vector<int>> p;

    for (int i = 0; i < n; ++i) {
        cin >> x[i];
        p[x[i]].push_back(i);
    }

    int a = x[0], l = 0, r = 0, msf = 1, cur, s;

    for (auto [v, idx] : p) {
        cur = 1, s = idx[0];
        for (int i = 1; i < idx.size(); ++i) {
            ++cur;
            cur -= idx[i] - idx[i - 1] - 1;
            if (cur < 1) {
                cur = 1;
                s = idx[i];
            }
            if (cur > msf) {
                a = v;
                l = s;
                r = idx[i];
                msf = cur;
            }
        }
    }

    cout << a << " " << (l + 1) << " " << (r + 1) << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}