/**
 * https://codeforces.com/contest/1327/problem/A
 * Time: O(1)
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

        int n, k;
        cin >> n >> k;

        if (1ll * k * k > n || ((n & 1) != (k & 1)))
            cout << "NO";
        else
            cout << "YES";
        cout << '\n';
    }
}
