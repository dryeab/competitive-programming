#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

/*

*/

void solve() {
    ll n;
    cin >> n;

    vector<ll> a(n);
    for (ll i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    if (a.size() == 1) {
        cout << "1\n";
        return;
    }

    ll g = 0;
    for (ll i = 1; i < n; ++i) {
        g = gcd(g, a[i] - a[i - 1]);
    }

    set<ll> s(a.begin(), a.end());

    ll mx = a.back();
    while (s.find(mx) != s.end())
        mx -= g;

    ll res = (a.back() - mx) / g;
    for (ll i = 0; i < n - 1; ++i)
        res += (a.back() - a[i]) / g;

    cout << res << "\n";
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t = 1;
    cin >> t;

    while (t--) {
        solve();
    }
}