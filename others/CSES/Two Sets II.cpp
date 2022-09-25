/**
 * https://cses.fi/problemset/task/1093/
 * Time: O(N^3)
 * Space: O(N^3)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MOD = 1e9 + 7;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int s = ((n + 1) * n) >> 1;

    if (s & 1) {
        cout << 0;
        return 0;
    }

    s >>= 1;

    int dp[n][s + 1];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= s; ++j) {
            if (j == 0)
                dp[i][j] = 1;
            else if (i == 0)
                dp[i][j] = 0;
            else {
                dp[i][j] = dp[i - 1][j];
                if (j - i >= 0)
                    (dp[i][j] += dp[i - 1][j - i]) %= MOD;
            }
        }
    }

    cout << dp[n - 1][s];
}