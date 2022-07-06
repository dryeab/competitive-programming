/**
 * https://codeforces.com/problemset/problem/1360/C
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    int n, i;
    cin >> n;

    int ok = false, odd = 0;
    vector<int> a(105);

    for (int x = n; x; --x) {
        cin >> i;
        if (a[i - 1] || a[i + 1]) {
            ok = true;
        }
        a[i] = 1;
        if (i & 1)
            odd++;
    }

    cout << ((ok || !(odd & 1)) ? "YES" : "NO") << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}