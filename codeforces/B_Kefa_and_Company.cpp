/**
 * https://codeforces.com/contest/580/problem/B
 * Time: O(nlog(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, d;
    cin >> n >> d;

    vector<pair<int, int>> f(n);
    for (int i = 0; i < n; ++i)
        cin >> f[i].first >> f[i].second;

    sort(f.begin(), f.end());

    ll res = 0, cur = 0;

    for (int i = 0, j = 0; i < n; ++i) {
        while (j < n && f[j].first - f[i].first < d) {
            cur += f[j++].second;
        }
        res = max(res, cur);
        cur -= f[i].second;
    }

    cout << res;
}