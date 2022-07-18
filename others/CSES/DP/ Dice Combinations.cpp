/**
 * https://cses.fi/problemset/task/1633/
 * Time: O(n)
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

    vector<int> dp(n + 1);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = i - 1; j >= i - 6 && j >= 0; j--) {
            dp[i] += dp[j];
            dp[i] %= MOD;
        }
    }

    cout << dp[n];
}