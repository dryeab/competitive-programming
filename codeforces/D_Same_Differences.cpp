/**
 * https://codeforces.com/contest/1520/problem/D
 * Time: O(N)
 * Space: O(N)
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

        map<int, int> cnt;
        ll res = 0;

        for (int i = 0; i < n; ++i) {
            cin >> a;
            res += cnt[a - i]++;
        }

        cout << res << '\n';
    }
}