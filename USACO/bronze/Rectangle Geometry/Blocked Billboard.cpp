/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=759
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    struct Rect {

        int x1, x2, y1, y2;

        int area() {
            return (x2 - x1) * (y2 - y1);
        }

        int intersection(Rect other) {
            int x = max(0, min(x2, other.x2) - max(x1, other.x1));
            int y = max(0, min(y2, other.y2) - max(y1, other.y1));
            return x * y;
        }
    };

    Rect billboard_1, billboard_2, truck;
    cin >> billboard_1.x1 >> billboard_1.y1 >> billboard_1.x2 >> billboard_1.y2;
    cin >> billboard_2.x1 >> billboard_2.y1 >> billboard_2.x2 >> billboard_2.y2;
    cin >> truck.x1 >> truck.y1 >> truck.x2 >> truck.y2;

    cout << billboard_1.area() + billboard_2.area() - truck.intersection(billboard_1) - truck.intersection(billboard_2);
}

void solve2() {

    int a, b, c, d, e, f, g, h, i, j, k, l;
    cin >> a >> b >> c >> d;
    cin >> e >> f >> g >> h;
    cin >> i >> j >> k >> l;

    int cnt = 0;
    for (int x = -1000; x <= 1000; ++x) {
        for (int y = -1000; y <= 1000; ++y) {
            if (i <= x && x < k && j <= y && y < l)
                continue;
            if (a <= x && x < c && b <= y && y < d)
                cnt++;
            else if (e <= x && x < g && f <= y && y < h)
                cnt++;
        }
    }

    cout << cnt;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("billboard.in", "r", stdin);
    freopen("billboard.out", "w", stdout);

    solve();
}