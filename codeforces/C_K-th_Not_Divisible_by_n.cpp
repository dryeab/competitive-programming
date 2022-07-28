/**
 * https://codeforces.com/contest/1352/problem/C
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

        if (k % (n - 1))
            cout << (n * (k / (n - 1)) + (k % (n - 1))) << '\n';
        else
            cout << n * (k / (n - 1)) - 1 << '\n';
    }
}