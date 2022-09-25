/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=1011
 * Time: O(N^3)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("triangles.in", "r", stdin);
    freopen("triangles.out", "w", stdout);

    int n;
    cin >> n;

    vector<int> x(n), y(n);
    for (int i = 0; i < n; ++i)
        cin >> x[i] >> y[i];

    int res = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                if (x[i] == x[j] && y[i] == y[k])
                    res = max(res, abs(x[k] - x[i]) * abs(y[i] - y[j]));
            }
        }
    }

    cout << res;
}