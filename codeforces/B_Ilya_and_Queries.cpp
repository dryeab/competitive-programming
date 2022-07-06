/**
 * https://codeforces.com/problemset/problem/313/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    int n = s.size();
    vector<int> dp(n + 1);

    for (int i = 2; i <= n; ++i)
        dp[i] = dp[i - 1] + (s[i - 1] == s[i - 2]);

    int m, l, r;
    cin >> m;

    for (int i = 0; i < m; ++i) {
        cin >> l >> r;
        cout << dp[r] - dp[l] << endl;
    }
}