/**
 * https://cses.fi/problemset/task/1635/
 * Time: O(xn)
 * Space: O(x + n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MOD = 1e9 + 7;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    int coins[n];
    for (int i = 0; i < n; ++i)
        cin >> coins[i];

    sort(coins, coins + n);

    int dp[x + 1] = {1};
    for (int i = 1; i <= x; ++i) {
        for (int j = 0; j < n && coins[j] <= i; ++j) {
            dp[i] += dp[i - coins[j]];
            dp[i] %= MOD;
        }
    }

    cout << dp[x];
}