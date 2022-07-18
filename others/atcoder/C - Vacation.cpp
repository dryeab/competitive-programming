/**
 * https://atcoder.jp/contests/dp/tasks/dp_c
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int act[n][3], dp[n][3];

    for (int i = 0; i < n; ++i)
        cin >> act[i][0] >> act[i][1] >> act[i][2];

    for (int j = 0; j < 3; ++j) {
        dp[0][j] = act[0][j];
    }

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            dp[i][j] = act[i][j] + max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]);
        }
    }

    cout << max({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]});
}