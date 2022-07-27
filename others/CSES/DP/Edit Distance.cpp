/**
 * https://cses.fi/problemset/task/1639/
 * Time: O(nm)
 * Space: O(nm)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s, t;
    cin >> s >> t;

    int n = s.size(), m = t.size();
    int dp[n + 1][m + 1];

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            if (i == 0 && j == 0)
                dp[0][0] = 0;
            else if (i == 0)
                dp[0][j] = j;
            else if (j == 0)
                dp[i][0] = i;
            else
                dp[i][j] = min({1 + dp[i][j - 1],
                                1 + dp[i - 1][j],
                                (s[i - 1] != t[j - 1]) + dp[i - 1][j - 1]});
        }
    }

    cout << dp[n][m];
}