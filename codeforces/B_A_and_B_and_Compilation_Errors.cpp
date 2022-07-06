/**
 * https://codeforces.com/problemset/problem/519/B
 * Time: O(n)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    int a = 0, b = 0, c = 0;

    for (int i = 0; i < n; ++i) {
        cin >> x;
        a += x;
    }

    for (int i = 0; i < n - 1; ++i) {
        cin >> x;
        b += x;
    }

    for (int i = 0; i < n - 2; ++i) {
        cin >> x;
        c += x;
    }

    cout << a - b << endl
         << b - c;
}