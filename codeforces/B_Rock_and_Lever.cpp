/**
 * https://codeforces.com/problemset/problem/1420/B
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

        ll n, a, res = 0;
        cin >> n;

        vector<int> cnt(32);
        for (int i = 0; i < n; ++i) {
            cin >> a;
            for (int j = 31; j >= 0; --j) {
                if ((a >> j) & 1) {
                    res += cnt[j], ++cnt[j];
                    break;
                }
            }
        }

        cout << res << "\n";
    }
}