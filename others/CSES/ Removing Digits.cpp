#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int dp[n + 1];
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        dp[i] = 1e9;
        for (int j = i; j; j /= 10)
            dp[i] = min(dp[i], dp[i - (j % 10)] + 1);
    }

    cout << dp[n];
}