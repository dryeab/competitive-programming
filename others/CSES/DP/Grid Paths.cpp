/**
 * https://cses.fi/problemset/task/1638/
 * Time: O(n^2)
 * Space: O(n)
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

    int dp[n];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char x;
            cin >> x;
            if (x == '*')
                dp[j] = 0;
            else if (i == 0 && j == 0)
                dp[0] = 1;
            else if (i == 0)
                dp[j] = dp[j - 1];
            else if (j == 0)
                continue;
            else
                (dp[j] += dp[j - 1]) %= MOD;
        }
    }

    cout << dp[n - 1];
}