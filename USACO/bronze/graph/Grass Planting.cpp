/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=894
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    // freopen("planting.in", "r", stdin);
    // freopen("planting.out", "w", stdout);

    int n;
    cin >> n;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    int res = 0;
    for (auto x : adj)
        res = max(res, (int)x.size() + 1);

    cout << res;
}