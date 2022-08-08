/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=663
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("square.in", "r", stdin);
    freopen("square.out", "w", stdout);

    int a, b, c, d, e, f, g, h;
    cin >> a >> b >> c >> d;
    cin >> e >> f >> g >> h;

    int xmn = min({a, c, e, g}), xmx = max({a, c, e, g});
    int ymn = min({b, d, f, h}), ymx = max({b, d, f, h});

    cout << (int)pow(max(ymx - ymn, xmx - xmn), 2);
}