/**
 * https://codeforces.com/problemset/problem/1328/B
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    ll n, k;
    cin >> n >> k;

    string res(n, 'a');

    for (ll i = 1; i < n; ++i) {
        if (k <= i) {
            res[i] = 'b';
            res[i - 1 - (i - k)] = 'b';
            break;
        }
        k -= i;
    }

    reverse(res.begin(), res.end());

    cout << res << "\n";
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;

    while (t--) {
        solve();
    }
}
