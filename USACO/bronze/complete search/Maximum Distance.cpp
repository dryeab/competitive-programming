/**
 * https://codeforces.com/gym/102951/problem/A
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MAX_N = 5005;
int x[MAX_N], y[MAX_N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int res = 0;

    for (int i = 0; i < n; ++i)
        cin >> x[i];

    for (int i = 0; i < n; ++i)
        cin >> y[i];

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int dx = x[i] - x[j], dy = y[i] - y[j];
            res = max(res, dx * dx + dy * dy);
        }
    }

    cout << res;
}