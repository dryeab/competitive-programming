/**
 * https://codeforces.com/contest/1690/problem/E
 * Time: O(n + k^2)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    int n, k;
    cin >> n >> k;

    vector<int> cnt(k);
    ll res = 0;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        res += x / k;
        cnt[x % k]++;
    }

    for (int i = 1; i < k; ++i) {
        for (int j = k - i; j < k && cnt[i] > 0; ++j) {
            int m;
            if (i != j)
                m = min(cnt[i], cnt[j]);
            else
                m = cnt[i] / 2;
            res += m, cnt[i] -= m, cnt[j] -= m;
        }
    }

    cout << res << '\n';
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}