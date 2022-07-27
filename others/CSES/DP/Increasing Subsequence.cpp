/**
 * https://cses.fi/problemset/task/1145/
 * Time: O(nlog(n))
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

    int x[n], K = 1e9 + 5;
    for (int i = 0; i < n; ++i)
        cin >> x[i];

    vector<int> dp(n, K);
    for (int i = 0; i < n; ++i)
        *lower_bound(dp.begin(), dp.end(), x[i]) = x[i];

    cout << (lower_bound(dp.begin(), dp.end(), K) - dp.begin());
}