/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=567
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int a, b, c, d;

void solve() {

    int total = (b - a) + (d - c);
    int intersection = max(0, min(b, d) - max(a, c));

    cout << total - intersection;
}

void solve3() {

    if (a > c)
        swap(a, c), swap(b, d);

    if (c >= b)
        cout << (d - c) + (b - a);
    else if (b < d)
        cout << d - a;
    else
        cout << b - a;
}

void solve2() {

    int cnt = 0;
    for (int i = 0; i <= 100; ++i)
        cnt += (a <= i && b > i) || (c <= i && d > i);

    cout << cnt;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("paint.in", "r", stdin);
    freopen("paint.out", "w", stdout);

    cin >> a >> b >> c >> d;

    solve(); // solve2(), solve3();
}