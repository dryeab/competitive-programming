/**
 * https://codeforces.com/group/ibNhxWfOek/contest/341358/problem/A
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

using namespace std;

void solve() {

    int n;
    cin >> n;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<int> res;
    for (int i = 1; i <= n; ++i) {
        if (res.size() >= i || a[i] == 0) {
            res.push_back(i);
        } else {
            if (i == 0 || a[i - 1] == 0) {
                res.push_back(n + 1);
            }
            res.push_back(i);
        }
    }

    if (res.size() <= n)
        res.push_back(n + 1);
        
    for (int x : res) {
        cout << x << " ";
    }

    cout << "\n";
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