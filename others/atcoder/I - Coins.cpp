/**
 * https://atcoder.jp/contests/dp/tasks/dp_i
 * Time: O(n^2)
 * Space: O(n^2)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    double p[n + 1];
    for (int i = 1; i <= n; ++i)
        cin >> p[i];

    double dp[n + 1][n + 1];
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= i; ++j) {
            if (i == 0 && j == 0)
                dp[0][0] = 1;
            else if (i == 0)
                dp[0][j] = 0;
            else if (j == 0)
                dp[i][0] = dp[i - 1][0] * (1 - p[i]);
            else
                dp[i][j] = (dp[i - 1][j] * (1 - p[i])) + (dp[i - 1][j - 1] * p[i]);
        }
    }

    double res = 0;
    for (int i = n; i > n / 2; --i)
        res += dp[n][i];

    cout << fixed << setprecision(10) << res;
}