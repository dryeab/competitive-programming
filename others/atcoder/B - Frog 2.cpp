/**
 * https://atcoder.jp/contests/dp/tasks/dp_b
 * Time: O(nk)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int h[n];
    for (int i = 0; i < n; ++i)
        cin >> h[i];

    int dp[n];
    dp[0] = 0;

    for (int i = 1; i < n; ++i) {
        dp[i] = INT32_MAX;
        for (int j = i - 1; j >= 0 && i - j <= k; --j)
            dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]));
    }

    cout << dp[n - 1];
}