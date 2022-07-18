/**
 * https://atcoder.jp/contests/dp/tasks/dp_e
 * Time: O(NV)
 * Space: O(NV)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, W, V = 0;
    cin >> n >> W;

    int w[n + 1], v[n + 1];
    for (int i = 1; i <= n; ++i) {
        cin >> w[i] >> v[i];
        V += v[i];
    }

    ll dp[n + 1][V + 1] = {};
    for (int i = 1; i <= V; ++i)
        dp[0][i] = 1e12;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= V; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j - v[i] >= 0 && (dp[i - 1][j - v[i]] + w[i] < dp[i][j]))
                dp[i][j] = dp[i - 1][j - v[i]] + w[i];
        }
    }

    for (int i = V; i >= 0; --i) {
        if (dp[n][i] <= W) {
            cout << i;
            return 0;
        }
    }
}