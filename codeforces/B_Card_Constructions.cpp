/**
 * https://codeforces.com/contest/1345/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        int n;
        cin >> n;

        int res = 0, h;
        while (n > 1) {
            h = 1;
            while (n >= (2 * h + h - 1)) {
                n -= 2 * h + h - 1;
                h++;
            }
            res++;
        }

        cout << res << '\n';
    }
}