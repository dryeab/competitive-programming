/**
 * https://atcoder.jp/contests/dp/tasks/dp_l
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

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    ll dp[n][n] = {};
    for (int i = n - 1; i >= 0; --i) {
        for (int j = i; j < n; ++j) {
            if (i == j)
                dp[i][j] = a[i];
            else
                dp[i][j] = max(a[i] - dp[i + 1][j], a[j] - dp[i][j - 1]);
        }
    }

    cout << dp[0][n - 1];
}