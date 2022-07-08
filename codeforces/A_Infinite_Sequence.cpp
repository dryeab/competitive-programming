/**
 * https://codeforces.com/problemset/problem/675/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    long long a, b, c;
    cin >> a >> b >> c;

    if (c < 0) {
        swap(a, b);
        c = -c;
    }

    if (c)
        cout << (a == b || (b > a && ((b - a) % c == 0)) ? "YES" : "NO");
    else
        cout << (b == a ? "YES" : "NO");
}