/**
 * https://codeforces.com/contest/580/problem/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int n, m, cnt;
vector<int> a;
vector<vector<int>> g;

void dfs(int i, int p, int nc) {

    if (a[i]) {
        if (nc == m)
            return;
        nc++;
    } else
        nc = 0;

    bool isLeaf = true;
    for (int x : g[i])
        if (x != p) {
            isLeaf = false;
            dfs(x, i, nc);
        }

    cnt += isLeaf;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;

    a.resize(n);
    g.resize(n);

    for (int &x : a)
        cin >> x;

    for (int i = 1; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        g[--x].push_back(--y);
        g[y].push_back(x);
    }

    dfs(0, -1, 0);

    cout << cnt;
}
