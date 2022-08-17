/**
 * https://codeforces.com/problemset/problem/1294/B
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n;
        cin >> n;

        vector<pair<int, int>> p(n);
        for (int i = 0; i < n; ++i)
            cin >> p[i].first >> p[i].second;

        sort(p.begin(), p.end());

        string res;
        int cx = 0, cy = 0, ok = true;

        for (auto [x, y] : p) {

            if (x < cx || y < cy) {
                ok = false;
                break;
            }

            res += string(x - cx, 'R');
            res += string(y - cy, 'U');

            cx = x, cy = y;
        }

        if (!ok)
            cout << "NO";
        else
            cout << "YES \n"
                 << res;
        cout << "\n";
    }
}