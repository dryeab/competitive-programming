/**
 * https://cses.fi/problemset/task/1745/
 * Time: O(n*s)
 * Space: O(n*s)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, s = 0;
    cin >> n;

    vector<int> x(n);
    for (int &i : x) {
        cin >> i;
        s += i;
    }

    vector<vector<bool>> dp(n + 1, vector<bool>(s + 1));

    for (int i = 0; i <= n; ++i)
        dp[i][0] = true;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= s; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j - x[i - 1] >= 0 && dp[i - 1][j - x[i - 1]])
                dp[i][j] = true;
        }
    }

    cout << (count(dp[n].begin(), dp[n].end(), true) - 1) << '\n';

    for (int i = 1; i <= s; ++i)
        if (dp[n][i])
            cout << i << ' ';
}