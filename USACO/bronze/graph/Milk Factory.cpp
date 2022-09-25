/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=940
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("factory.in", "r", stdin);
    freopen("factory.out", "w", stdout);

    int n;
    cin >> n;

    vector<vector<int>> adj(n + 1);
    vector<int> cnt(n + 1), indegree(n + 1);

    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        indegree[b]++;
    }

    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {

        int i = q.front();
        q.pop();

        for (int j : adj[i]) {
            cnt[j] += cnt[i] + 1;
            indegree[j]--;
            if (indegree[j] == 0) {
                q.push(j);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (cnt[i] == n - 1) {
            cout << i;
            return 0;
        }
    }

    cout << -1;
}