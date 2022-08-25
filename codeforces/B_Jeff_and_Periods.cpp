/**
 * https://codeforces.com/problemset/problem/352/B
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, N = 1e5 + 1;
    cin >> n;

    vector<vector<int>> a(N);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        a[x].push_back(i);
    }

    vector<pair<int, int>> res;
    for (int i = 1; i < N; ++i) {
        if (a[i].size() == 0)
            continue;
        else if (a[i].size() == 1)
            res.push_back({i, 0});
        else {
            int d = a[i][1] - a[i][0], ok = true;
            for (int j = 2; j < a[i].size() && ok; ++j) {
                if (a[i][j] - a[i][j - 1] != d)
                    ok = false;
            }
            if (ok)
                res.push_back({i, d});
        }
    }

    cout << res.size() << "\n";
    for (auto [i, d] : res)
        cout << i << ' ' << d << "\n";
}