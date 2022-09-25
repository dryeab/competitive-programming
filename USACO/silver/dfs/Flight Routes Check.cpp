/**
 * https://cses.fi/problemset/task/1682/
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e5 + 5;
vector<int> adj1[N], adj2[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj1[a].push_back(b);
        adj2[b].push_back(a);
    }

    int adj;
    vector<bool> visited(n + 1);

    function<void(int)> dfs = [&](int i) {
        visited[i] = true;
        for (int j : (adj == 1 ? adj1 : adj2)[i]) {
            if (!visited[j])
                dfs(j);
        }
    };

    adj = 1, dfs(1);

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            cout << "NO\n";
            cout << 1 << ' ' << i;
            return 0;
        }
    }

    adj = 2, fill(visited.begin(), visited.end(), false), dfs(1);

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            cout << "NO\n";
            cout << i << ' ' << 1;
            return 0;
        }
    }

    cout << "YES";
}