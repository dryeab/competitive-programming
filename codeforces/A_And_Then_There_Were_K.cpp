/**
 * https://codeforces.com/contest/1527/problem/A
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

        int n;
        cin >> n;

        int cnt = 0;
        while (n)
            cnt++, n >>= 1;

        cout << (1 << (cnt - 1)) - 1 << '\n';
    }
}