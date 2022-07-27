/**
 * https://codeforces.com/problemset/problem/1606/B
 * Time: O(log(k))
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

        ll n, k;
        cin >> n >> k;

        ll cur = 1, res = 0;
        while (cur < n) {
            if (cur < k) {
                cur <<= 1;
                res++;
            } else {
                res += (n - cur + k - 1) / k;
                break;
            }
        }

        cout << res << '\n';
    }
}