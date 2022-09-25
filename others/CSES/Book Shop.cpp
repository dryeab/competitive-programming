/**
 * https://cses.fi/problemset/task/1158/
 * Time: O(nx)
 * Space: O(nx)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    vector<int> h(n), s(n);
    for (int &x : h)
        cin >> x;
    for (int &x : s)
        cin >> x;

    vector<vector<int>> dp(n + 1, vector<int>(x + 1));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= x; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (h[i - 1] <= j && s[i - 1] + dp[i - 1][j - h[i - 1]] > dp[i][j])
                dp[i][j] = s[i - 1] + dp[i - 1][j - h[i - 1]];
        }
    }

    cout << dp[n][x];
}