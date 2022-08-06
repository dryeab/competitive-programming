/**
 * https://codeforces.com/problemset/problem/977/C
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    sort(a, a + n);

    if (k == 0) {
        if (a[0] == 1)
            cout << -1;
        else
            cout << a[0] - 1;
    } else if (k == n) {
        cout << a[n - 1];
    } else {
        if (a[k - 1] == a[k])
            cout << -1;
        else {
            cout << a[k - 1];
        }
    }
}