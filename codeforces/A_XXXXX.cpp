/**
 * https://codeforces.com/contest/1364/problem/A
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n, x;
        cin >> n >> x;

        int a, sum = 0, mn = -1, mx = -1;
        for (int i = 1; i <= n; ++i) {

            cin >> a;
            sum += a;

            if (a % x) {
                if (mn == -1)
                    mn = i;
                mx = i;
            }
        }

        if (sum % x)
            cout << n;
        else if (mn == -1)
            cout << -1;
        else
            cout << max(n - mn, mx - 1);

        cout << '\n';
    }
}