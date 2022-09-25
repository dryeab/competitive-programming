/**
 * https://codeforces.com/problemset/problem/476/B
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll comb(ll n, ll r) {

    if (r == 0)
        return 1;

    if (n == r)
        return 1;

    ll res = 1;

    for (ll i = n; i > n - r; --i)
        res *= i;

    for (ll i = 1; i <= r; ++i)
        res /= i;

    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s1, s2;
    cin >> s1 >> s2;

    ll cor = 0;
    for (char c : s1) {
        if (c == '+')
            cor++;
        else
            cor--;
    }

    ll rec = 0, unc = 0;
    for (char c : s2) {
        if (c == '+')
            rec++;
        else if (c == '-')
            rec--;
        else
            unc++;
    }

    if (unc == 0) {
        cout << (rec == cor);
    } else {
        ll pos = 0, total = 0;
        for (ll i = 0; i <= unc; ++i) {
            ll ways = comb(unc, i);
            if ((rec + i - (unc - i)) == cor)
                pos += ways;
            total += ways;
        }
        cout << fixed << setprecision(15) << ((1.0 * pos) / (total));
    }
}