/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=569
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("badmilk.in", "r", stdin);
    freopen("badmilk.out", "w", stdout);

    int n, m, d, s;
    cin >> n >> m >> d >> s;

    vector<vector<pair<int, int>>> drink(n + 1);

    for (int i = 0; i < d; ++i) {

        int p, m, t;
        cin >> p >> m >> t;

        drink[p].push_back({t, m});
    }

    vector<int> pos(m + 1);

    for (int i = 0; i < s; ++i) {

        int p, t;
        cin >> p >> t;

        set<int> visited;
        for (auto x : drink[p]) {
            if (x.first < t) {
                visited.insert(x.second);
            }
        }

        for (int x : visited)
            pos[x]++;
    }

    int res = 0;
    for (int i = 1; i <= m; ++i) {

        if (pos[i] != s)
            continue;

        set<int> cnt;
        for (int j = 1; j <= n; ++j) {
            for (auto x : drink[j]) {
                if (x.second == i) {
                    cnt.insert(j);
                }
            }
        }
        res = max(res, (int)cnt.size());
    }

    cout << res;
}