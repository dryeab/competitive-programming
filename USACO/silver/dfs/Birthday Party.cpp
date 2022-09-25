/**
 * https://open.kattis.com/problems/birthday
 * Time: O(NM + M^2)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    while (n || m) {

        vector<vector<int>> adj(n);
        vector<pair<int, int>> edges;

        for (int i = 0; i < m; ++i) {

            int a, b;
            cin >> a >> b;

            adj[a].push_back(b);
            adj[b].push_back(a);

            edges.push_back({a, b});
        }

        int a, b;

        function<int(int, vector<bool> &)> dfs = [&](int i, vector<bool> &visited) {
            visited[i] = true;
            int res = 1;
            for (int j : adj[i]) {
                if (!visited[j] && !((a == i && b == j) || (a == j && b == i)))
                    res += dfs(j, visited);
            }
            return res;
        };

        bool ok = true;
        for (auto edge : edges) {

            a = edge.first, b = edge.second;

            vector<bool> visited(n);

            if (dfs(0, visited) < n) {
                ok = false;
                break;
            }
        }

        cout << (ok ? "NO" : "YES") << "\n";

        cin >> n >> m;
    }
}
