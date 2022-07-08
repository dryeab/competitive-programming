/**
 * https://codeforces.com/problemset/problem/1417/B
 * Time: O(n)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using ll = long long;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int test;
    cin >> test;

    while (test--) {

        int n, t, x, m = 0;
        cin >> n >> t;

        for (int i = 0; i < n; ++i) {
            cin >> x;
            if (2 * x == t) {
                cout << (m++ % 2) << " ";
            } else if (x <= t / 2) {
                cout << 0 << " ";
            } else {
                cout << 1 << " ";
            }
        }
        cout << "\n";
    }
}