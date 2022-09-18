/**
 * https://codeforces.com/problemset/problem/1360/D
 * Time: O(sqrt(n))
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int solve() {

    int n, k, res;
    cin >> n >> k;

    res = n;

    if (k >= n)
        return 1;

    for (int i = 1; i <= sqrt(n) && i <= k; ++i) {
        if (n % i)
            continue;
        res = min(res, n / i);
        if (n / i <= k)
            res = min(res, i);
    }

    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        cout << solve() << '\n';
    }
}
