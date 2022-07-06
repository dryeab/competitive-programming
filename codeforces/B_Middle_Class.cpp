/**
 * https://codeforces.com/contest/1334/problem/B
 * Time: O(nlog(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, x;
    cin >> n >> x;

    vector<int> a(n);
    for (int &i : a)
        cin >> i;

    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());

    long long res = 0, sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += a[i];
        if ((sum / (i + 1)) >= x)
            res++;
        else
            break;
    }

    cout << res << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}