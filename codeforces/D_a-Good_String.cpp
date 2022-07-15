/**
 * https://codeforces.com/contest/1385/problem/D
 * Time: O(nlog(n))
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int solve(string &s, int i, int j, char c) {

    if (i == j)
        return s[i] != c;

    int res = 1e6, d = 0, m = (i + j) / 2 + 1;

    for (int k = i; k < m; ++k) {
        if (s[k] != c)
            d++;
    }

    res = d + solve(s, m, j, c + 1);

    d = 0;
    for (int k = m; k <= j; ++k) {
        if (s[k] != c)
            d++;
    }
    res = min(res, d + solve(s, i, m - 1, c + 1));

    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        cout << solve(s, 0, n - 1, 'a') << '\n';
    }
}