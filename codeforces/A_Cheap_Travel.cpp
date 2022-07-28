/**
 * https://codeforces.com/problemset/problem/466/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, a, b;
    cin >> n >> m >> a >> b;

    int x = min(m * a, b);

    cout << (n / m * x + min((n % m) * a, b));
}