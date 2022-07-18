/**
 * https://atcoder.jp/contests/dp/tasks/dp_h
 * Time: O(hw)
 * Space: O(w)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MOD = 1e9 + 7;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int h, w;
    cin >> h >> w;

    int dp[w + 1] = {};
    char x;
    for (int i = 1; i <= h; ++i) {
        for (int j = 1; j <= w; ++j) {
            cin >> x;
            if (i == 1 && j == 1)
                dp[j] = 1;
            else if (x == '.')
                (dp[j] += dp[j - 1]) %= MOD;
            else
                dp[j] = 0;
        }
    }

    cout << dp[w];
}