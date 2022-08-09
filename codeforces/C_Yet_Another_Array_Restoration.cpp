/**
 * https://codeforces.com/problemset/problem/1409/C
 * Time: O(N + (y - x))
 * Space: O(N)
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

        int n, x, y;
        cin >> n >> x >> y;

        for (int d = 1; d <= y - x; ++d) {
            if ((y - x) % d == 0 && (y - x) / d < n) {

                vector<int> res;

                for (int i = x; n && i <= y; i += d, n--)
                    res.push_back(i);

                for (int i = x - d; i > 0 && n; i -= d, n--)
                    res.push_back(i);

                for (int i = y + d; n; i += d, n--)
                    res.push_back(i);

                for (int i : res)
                    cout << i << ' ';

                cout << '\n';

                break;
            }
        }
    }
}