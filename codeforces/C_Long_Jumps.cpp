/**
 * https://codeforces.com/problemset/problem/1472/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 5;
int a[N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t, n, res;
    cin >> t;

    while (t--) {

        cin >> n;
        res = 0;

        for (int i = 0; i < n; ++i)
            cin >> a[i];

        for (int i = n - 1; i >= 0; --i) {
            a[i] += (i + a[i] < n ? a[i + a[i]] : 0);
            res = max(res, a[i]);
        }

        cout << res << endl;
    }
}