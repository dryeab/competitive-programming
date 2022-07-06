/**
 * https://codeforces.com/contest/363/problem/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<int> h(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> h[i];
        h[i] += h[i - 1];
    }

    int res = -1, msf = 1e9;
    for (int i = k; i <= n; ++i) {
        if (h[i] - h[i - k] < msf) {
            res = i - k + 1;
            msf = h[i] - h[i - k];
        }
    }

    cout << res;
}