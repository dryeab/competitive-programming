/**
 * https://codeforces.com/problemset/problem/1400/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    string s;
    cin >> s;

    int x, n = s.size();
    cin >> x;

    int res[n] = {};
    for (int i = 0; i < n; ++i)
        res[i] = -1;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') {
            if (i - x >= 0)
                res[i - x] = 0;
            if (i + x < n)
                res[i + x] = 0;
        }
    }

    bool ok = true;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            int cnt = 0;
            if (i - x >= 0 && res[i - x] != 0) {
                res[i - x] = 1;
                cnt++;
            }
            if (i + x < n && res[i + x] != 0) {
                res[i + x] = 1;
                cnt++;
            }
            if (cnt == 0) {
                ok = false;
                break;
            }
        }
    }

    if (!ok) {
        cout << -1 << '\n';
        return;
    }

    for (int i = 0; i < n; ++i)
        if (res[i] == -1)
            cout << 0;
        else
            cout << res[i];
    cout << '\n';
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}