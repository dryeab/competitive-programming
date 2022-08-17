/**
 * https://codeforces.com/problemset/problem/285/C
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    sort(a.begin(), a.end());

    ll res = 0;
    for (int i = 0; i < n; ++i)
        res += abs(i + 1 - a[i]);

    cout << res;
}