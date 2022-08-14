/**
 * https://codeforces.com/contest/1421/problem/A
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

        int a, b;
        cin >> a >> b;

        cout << (a ^ b) << '\n';
    }
}