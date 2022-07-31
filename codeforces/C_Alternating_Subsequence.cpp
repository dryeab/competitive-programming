/**
 * https://codeforces.com/contest/1343/problem/C
 * Time: O(n)
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

        int n;
        cin >> n;
        
        ll res = 0, M, a;
        cin >> M;
        for (int i = 1; i < n; ++i) {
            cin >> a;
            if (a * M < 0) {
                res += M;
                M = a;
            }
            M = max(M, a);
        }

        cout << res + M << '\n';
    }
}