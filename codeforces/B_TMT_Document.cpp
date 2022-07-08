/**
 * https://codeforces.com/problemset/problem/1509/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

bool solve() {

    int n, ok = true, t = 0, m = 0;
    cin >> n;

    string s;
    cin >> s;

    for (int i = 0; i < n; ++i) {
        if (s[i] == 'T')
            t++;
        else
            m++;
        if (m > t)
            return false;
    }

    t = 0, m = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == 'T')
            t++;
        else
            m++;
        if (m > t)
            return false;
    }

    return ok && (t == n / 3 * 2);
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        cout << (solve() ? "YES" : "NO") << '\n';
    }
}