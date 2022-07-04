/**
 * https://codeforces.com/problemset/problem/1676/D
 * Time: O(nm)
 * Space: O(nm)
 */

#include <bits/stdc++.h>

int grid[201][201];

using namespace std;

void solve() {
    int n, m;
    scanf("%d %d", &n, &m);

    map<int, int> right, left;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &grid[i][j]);
            right[i + j] += grid[i][j];
            left[i - j] += grid[i][j];
        }
    }

    int res = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            res = max(res, right[i + j] + left[i - j] - grid[i][j]);

    printf("%d \n", res);
}

int main() {

    int t;
    scanf("%d", &t);

    while (t--)
        solve();
}
