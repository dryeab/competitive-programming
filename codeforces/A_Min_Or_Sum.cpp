/**
 * https://codeforces.com/problemset/problem/1635/A
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n, a;
        cin >> n;

        int res = 0;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            res |= a;
        }

        cout << res << '\n';
    }
}