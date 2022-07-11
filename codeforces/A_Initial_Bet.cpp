/**
 * https://codeforces.com/contest/478/problem/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int x, s = 0;
    for (int i = 0; i < 5; ++i) {
        cin >> x;
        s += x;
    }

    if (!s || s % 5)
        cout << -1;
    else
        cout << (s / 5);
}