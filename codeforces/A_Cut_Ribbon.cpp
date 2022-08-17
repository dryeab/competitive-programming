/**
 * https://codeforces.com/problemset/problem/189/A
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, a, b, c;
    cin >> n >> a >> b >> c;

    vector<int> dp(n + 1, INT_MIN);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        if (i >= a)
            dp[i] = max(dp[i], dp[i - a] + 1);
        if (i >= b)
            dp[i] = max(dp[i], dp[i - b] + 1);
        if (i >= c)
            dp[i] = max(dp[i], dp[i - c] + 1);
    }

    cout << dp[n];
}