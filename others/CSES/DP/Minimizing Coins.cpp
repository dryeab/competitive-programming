/**
 * https://cses.fi/problemset/task/1634/
 * Time: O(xn)
 * Space: O(x + n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    vector<int> coins(n);
    for (int &coin : coins)
        cin >> coin;

    vector<int> dp(x + 1, -1);
    dp[0] = 0;

    for (int i = 1; i <= x; ++i) {
        for (int coin : coins)
            if (i - coin >= 0 && dp[i - coin] != -1 && (dp[i] == -1 || dp[i] > dp[i - coin] + 1))
                dp[i] = dp[i - coin] + 1;
    }

    cout << dp[x];
}