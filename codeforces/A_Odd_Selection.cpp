/**
 * https://codeforces.com/problemset/problem/1363/A
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

bool solve() {

    int n, x;
    cin >> n >> x;

    int a, even = 0, odd = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a;
        (a & 1 ? odd : even)++;
    }

    for (int i = 1; i <= odd && i <= x; i += 2)
        if (x - i <= even)
            return true;

    return false;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        cout << (solve() ? "YES" : "NO") << '\n';
    }
}