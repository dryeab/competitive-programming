/**
 * https://codeforces.com/problemset/problem/519/C
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int ans = 0;
    for (int i = 0; i <= n && 2 * i <= m; i++) {
        int ln = n - i, lm = m - 2 * i;
        ans = max(ans, i + min(ln / 2, lm));
    }

    cout << ans;
}