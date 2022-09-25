/**
 * https://cses.fi/problemset/task/1623/
 * Time: (2^N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll p[20];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;

    for (ll i = 0; i < n; ++i)
        cin >> p[i];

    ll sum = accumulate(p, p + n, 0LL);
    ll res = sum;

    for (ll mask = 0; mask < (1 << n); ++mask) {
        ll ssf = 0;
        for (ll i = 0; i < n; ++i) {
            if ((mask >> i) & 1)
                ssf += p[i];
        }
        res = min(res, abs(sum - ssf - ssf));
    }

    cout << res;
}
