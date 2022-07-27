/**
 * https://codeforces.com/contest/1332/problem/A
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

        int a, b, c, d, x, y, x1, x2, y1, y2;
        cin >> a >> b >> c >> d >> x >> y >> x1 >> y1 >> x2 >> y2;

        if (x - a + b >= x1 && (x1 != x2 || a + b == 0) && x + b - a <= x2 && (y1 != y2 || c + d == 0) && y - c + d >= y1 && y + d - c <= y2)
            cout << "YES";
        else
            cout << "NO";

        cout << "\n";
    }
}