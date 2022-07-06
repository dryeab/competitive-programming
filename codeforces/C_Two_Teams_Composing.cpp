/**
 * https://codeforces.com/problemset/problem/1335/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    int n, x;
    cin >> n;

    vector<int> cnt(n + 1);
    for (int i = n; i; --i) {
        cin >> x;
        cnt[x]++;
    }

    int mx = *max_element(cnt.begin(), cnt.end());
    int uni = n + 1 - count(cnt.begin(), cnt.end(), 0);

    cout << max(min(uni - 1, mx), min(mx - 1, uni)) << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}