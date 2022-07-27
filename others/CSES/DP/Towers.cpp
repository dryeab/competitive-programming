/**
 * https://cses.fi/problemset/task/1073/
 * Time: O(nlog(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, C = 1e9 + 2;
    cin >> n;

    int k[n];
    for (int i = 0; i < n; ++i)
        cin >> k[i];

    vector<int> dp(n, C);
    for (int i = 0; i < n; ++i)
        *upper_bound(dp.begin(), dp.end(), k[i]) = k[i];

    cout << (lower_bound(dp.begin(), dp.end(), C) - dp.begin());
}