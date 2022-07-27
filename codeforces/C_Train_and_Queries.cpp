/**
 * https://codeforces.com/contest/1702/problem/C
 * Time: O(nk)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    int n, k;
    cin >> n >> k;

    map<int, int> first, last;

    for (int i = 1; i <= n; ++i) {

        int x;
        cin >> x;

        if (!first.count(x))
            first[x] = i;

        last[x] = i;
    }

    for (int i = 0; i < k; ++i) {

        int a, b;
        cin >> a >> b;

        if (first.count(a) && first.count(b) && first[a] <= last[b])
            cout << "YES";
        else
            cout << "NO";

        cout << '\n';
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}