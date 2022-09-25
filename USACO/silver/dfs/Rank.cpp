/**
 * https://dmoj.ca/problem/acsl1p4
 * Time: O(N + M)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<vector<int>> adj(n + 1);
    while (k--) {
        int a, b, sa, sb;
        cin >> a >> b >> sa >> sb;
        if (sa > sb)
            adj[a].push_back(b);
        else
            adj[b].push_back(a);
    }

    vector<int> state(n + 1), next(n + 1);
    unordered_set<int> res;

    function<void(int)> dfs = [&](int i) {
        state[i] = 1;
        for (int j : adj[i]) {
            if (state[j] == 2) {
                continue;
            } else if (state[j] == 1) {
                while (j) {
                    res.insert(j);
                    j = next[j];
                }
            } else {
                next[i] = j;
                dfs(j);
                next[i] = 0;
            }
        }
        state[i] = 2;
    };

    for (int i = 1; i <= n; ++i) {
        if (state[i] == 0) {
            dfs(i);
        }
    }

    cout << res.size();
}
