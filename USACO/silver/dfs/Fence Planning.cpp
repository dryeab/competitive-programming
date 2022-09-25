/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=944
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e5 + 5;
vector<int> adj[N];
pair<int, int> cord[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("fenceplan.in", "r", stdin);
    freopen("fenceplan.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; ++i)
        cin >> cord[i].first >> cord[i].second;

    for (int i = 0; i < m; ++i) {

        int a, b;
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    int p = INT_MAX, x_min, x_max, y_min, y_max;
    vector<bool> visited(n + 1);

    function<void(int)> dfs = [&](int i) {
        x_min = min(x_min, cord[i].first);
        x_max = max(x_max, cord[i].first);
        y_min = min(y_min, cord[i].second);
        y_max = max(y_max, cord[i].second);

        visited[i] = true;
        for (int j : adj[i]) {
            if (!visited[j])
                dfs(j);
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (visited[i])
            continue;
        x_min = INT_MAX, y_min = INT_MAX, y_max = INT_MIN, x_max = INT_MIN;
        dfs(i);
        p = min(p, 2 * (x_max - x_min) + 2 * (y_max - y_min));
    }

    cout << p;
}
