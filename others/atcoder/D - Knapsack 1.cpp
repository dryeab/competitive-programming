/**
 * https://atcoder.jp/contests/dp/tasks/dp_d
 * Time: O(NW)
 * Space: O(NW)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, W;
    cin >> n >> W;

    int v[n + 1], w[n + 1];
    for (int i = 1; i <= n; ++i)
        cin >> w[i] >> v[i];

    vector<vector<ll>> dp(n + 1, vector<ll>(W + 1));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= W; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j - w[i] >= 0 && dp[i - 1][j - w[i]] + v[i] > dp[i][j])
                dp[i][j] = dp[i - 1][j - w[i]] + v[i];
        }
    }

    cout << dp[n][W];
}