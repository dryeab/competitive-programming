/**
 * https://codeforces.com/problemset/problem/958/B1
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> deg(n + 1);

    int u, v;
    for (int i = 0; i < n - 1; ++i) {
        cin >> u >> v;
        deg[u]++;
        deg[v]++;
    }

    int res = 0;
    for (auto x : deg)
        res += (x == 1);

    cout << res << endl;
}