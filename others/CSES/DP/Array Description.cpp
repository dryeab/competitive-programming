/**
 * https://cses.fi/problemset/task/1746/
 * Time: O(nm)
 * Space: O(mn)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MOD = 1e9 + 7;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int x[n];
    for (int i = 0; i < n; ++i)
        cin >> x[i];

    vector<vector<ll>> dp(n, vector<ll>(m + 2));

    // base case
    if (x[0])
        dp[0][x[0]] = 1;
    else
        for (int i = 1; i <= m; ++i)
            dp[0][i] = 1;

    for (int i = 1; i < n; ++i) {

        if (x[i]) {
            (dp[i][x[i]] = dp[i - 1][x[i] - 1] + dp[i - 1][x[i]] + dp[i - 1][x[i] + 1]) %= MOD;
            continue;
        }

        for (int j = 1; j <= m; ++j) {
            (dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) %= MOD;
        }
    }

    cout << (accumulate(dp[n - 1].begin(), dp[n - 1].end(), 0ll) % MOD);
}