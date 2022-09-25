/**
 * https://codeforces.com/problemset/problem/230/B
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    const ll MAX_N = 1e6 + 10;
    bool isPrime[MAX_N];

    for (ll i = 2; i < MAX_N; ++i) {
        if (!isPrime[i])
            continue;
        for (ll j = 2; i * j < MAX_N; ++j)
            isPrime[i * j] = false;
    }

    ll n, x;
    cin >> n;

    for (ll i = 0; i < n; ++i) {
        cin >> x;
        ll s = (int)sqrt(x);
        if (s * s == x && isPrime[s] && s != 1)
            cout << "YES";
        else
            cout << "NO";
        cout << "\n";
    }
}