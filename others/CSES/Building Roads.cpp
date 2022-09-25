/**
 * https://cses.fi/problemset/task/1666/
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e5 + 6;
vector<int> adj[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<bool> visited(n + 1, false);

    function<void(int)> dfs;
    dfs = [&](int i) {
        visited[i] = true;
        for (int j : adj[i]) {
            if (!visited[j])
                dfs(j);
        }
    };

    vector<int> res;
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(i);
            res.push_back(i);
        }
    }

    cout << res.size() - 1 << "\n";
    for (int i = 1; i < (int)res.size(); ++i)
        cout << res[i] << ' ' << res[i - 1] << "\n";
}
