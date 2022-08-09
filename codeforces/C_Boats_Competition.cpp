/**
 * https://codeforces.com/problemset/problem/1399/C
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

        int n, x;
        cin >> n;

        map<int, int> w;
        for (int i = 0; i < n; ++i) {
            cin >> x;
            w[x]++;
        }

        int k = 0;
        for (int s = 2; s <= 2 * n; ++s) {
            int cur = 0;
            for (auto [x, cnt] : w) {
                if (w.count(s - x)) {
                    cur += min(cnt, w[s - x]);
                }
            }
            k = max(k, cur / 2);
        }

        cout << k << '\n';
    }
}