/**
 * https://atcoder.jp/contests/dp/tasks/dp_f
 * Time: O(nm)
 * Space: O(nm)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s, t;
    cin >> s >> t;

    int n = s.size(), m = t.size();
    int dp[n + 1][m + 1] = {};

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    int i = n, j = m;
    string res = "";

    while (dp[i][j] && i && j) {
        if (s[i - 1] == t[j - 1]) {
            res.push_back(s[i - 1]);
            i--, j--;
        } else if (dp[i - 1][j] > dp[i][j - 1])
            i--;
        else
            j--;
    }

    reverse(res.begin(), res.end());

    cout << res;
}