/**
 * https://codeforces.com/problemset/problem/1324/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    int n, x, ok = false;
    cin >> n;

    map<int, int> store;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (store.count(x)) {
            if (i - store[x] > 1)
                ok = true;
        } else {
            store[x] = i;
        }
    }
    cout << (ok ? "YES" : "NO") << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}