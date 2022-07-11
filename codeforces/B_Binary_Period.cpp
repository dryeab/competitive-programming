/**
 * https://codeforces.com/contest/1342/problem/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    string t;
    cin >> t;

    for (int i = 1; i < t.size(); ++i) {
        if (t[i - 1] != t[i]) {
            for (int j = 0; j < t.size(); ++j) {
                cout << "01";
            }
            return;
        }
    }
    cout << t;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        // cout << "ans ";
        solve();
        cout << '\n';
    }
}