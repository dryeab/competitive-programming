/**
 * https://atcoder.jp/contests/dp/tasks/dp_k
 * Time: O(nk)
 * Space: O(n + k)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    vector<bool> dp(k + 1, false);
    for (int i = 1; i <= k; ++i) {
        for (int j = 0; j < n && a[j] <= i; ++j) {
            if (!dp[i - a[j]]) {
                dp[i] = true;
                break;
            }
        }
    }

    cout << (dp[k] ? "First" : "Second");
}