/**
 * https://codeforces.com/problemset/problem/1324/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    string s;
    cin >> s;

    int l = -1, res = 0, n = s.size();
    for (int i = 0; i <= n; ++i) {
        if (i == n || s[i] == 'R') {
            res = max(res, i - l);
            l = i;
        }
    }

    cout << res << endl;
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