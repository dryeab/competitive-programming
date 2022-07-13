/**
 * https://codeforces.com/contest/276/problem/C
 * Time: O(nlog(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    sort(a, a + n);

    int cnt[n] = {};
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--, r--;
        cnt[l]++;
        if (r + 1 < n)
            cnt[r + 1]--;
    }

    for (int i = 1; i < n; ++i)
        cnt[i] += cnt[i - 1]; // prefix sum

    sort(cnt, cnt + n);

    ll res = 0;
    for (int i = n - 1; i >= 0; i--)
        res += 1ll * a[i] * cnt[i];

    cout << res;
}