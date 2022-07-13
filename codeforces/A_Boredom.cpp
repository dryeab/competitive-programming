/**
 * https://codeforces.com/problemset/problem/455/A
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e5 + 1;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    vector<ll> cnt(N), dp(N);
    for (int i = 0; i < n; ++i) {
        cin >> x;
        cnt[x]++;
    }

    dp[1] = cnt[1];

    for (int i = 2; i < N; ++i) {
        dp[i] = max(dp[i - 1], dp[i - 2] + cnt[i] * i);
    }

    cout << dp[N - 1];
}
