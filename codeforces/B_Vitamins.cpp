/**
 * https://codeforces.com/contest/1042/problem/B
 * Time: 
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int> m(8, 1e8);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {

        int c;
        string s;

        cin >> c >> s;

        int j = 0;
        for (char x : s) {
            if (x == 'A')
                j |= (1 << 2);
            else if (x == 'B')
                j |= (1 << 1);
            else
                j |= 1;
        }

        m[j] = min(m[j], c);
    }

    int res = 1e8;
    for (int mask = 0; mask < (1 << 8); ++mask) {
        int j = 0, ct = 0;
        for (int i = 0; i < 8; ++i) {
            if (mask & (1 << i)) {
                j |= i;
                ct += m[i];
            }
        }

        if (j == 7)
            res = min(res, ct);
    }

    cout << (res == (int)1e8 ? -1 : res);
}