/**
 * https://codeforces.com/contest/977/problem/E
 * Time: O(|V| + |E|)
 * Space: O(|V| + |E|)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int dfs(int i, int p, vector<vector<int>> &graph, vector<int> &visited) {

    if (visited[i])
        return 1;

    visited[i] = 1;
    int res = 1;
    for (int neighbor : graph[i])
        if (neighbor != p)
            if (!dfs(neighbor, i, graph, visited))
                res = 0;

    return res && (graph[i].size() == 2);
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> visited(n);
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            res += dfs(i, -1, graph, visited);
        }
    }

    cout << res << '\n';
}