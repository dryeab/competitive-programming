/**
 * https://codeforces.com/problemset/problem/723/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b >> c;

    cout << max({a, b, c}) - min({a, b, c});
}