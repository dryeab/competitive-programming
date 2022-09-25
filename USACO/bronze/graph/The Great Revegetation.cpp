/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=916
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("revegetate.in", "r", stdin);
    freopen("revegetate.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<int> seed(n + 1);
    seed[1] = 1;

    for (int i = 2; i <= n; ++i) {

        set<int> used;
        for (int j : adj[i])
            used.insert(seed[j]);

        int pos = 1;
        while (used.count(pos))
            pos++;

        seed[i] = pos;
    }

    for (int i = 1; i <= n; ++i)
        cout << seed[i];
}