/**
 * https://codeforces.com/problemset/problem/610/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    if (n & 1) {
        cout << 0;
        return 0;
    }

    n /= 2;

    cout << (n & 1 ? n / 2 : n / 2 - 1);
}