/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=644
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 3005;
vector<int> adj[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("closing.in", "r", stdin);
    freopen("closing.out", "w", stdout);

    int n, m, x;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<bool> closed(n + 1, false);

    function<int(int, vector<bool> &)> dfs;
    dfs = [&](int i, vector<bool> &visited) {
        if (closed[i] || visited[i])
            return 0;

        visited[i] = true;

        int res = 1;
        for (int j : adj[i])
            res += dfs(j, visited);

        return res;
    };

    for (int j = 0; j < n; ++j) {

        for (int i = 1; i <= n; ++i) {
            if (!closed[i]) {
                vector<bool> visited(n + 1);
                cout << (dfs(i, visited) == n - j ? "YES" : "NO") << "\n";
                break;
            }
        }

        cin >> x;

        closed[x] = true;
    }
}
