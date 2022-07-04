/**
 * https://codeforces.com/problemset/problem/178/A1
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    int x, t, res = 0;

    for (int i = 0; i < n; ++i) {
        cin >> x;
        a[i] += x;

        t = floor(log2(n - 1 - i));

        a[i + pow(2, t)] += a[i];
        res += a[i];

        if (i != n - 1)
            cout << res << endl;
    }
}