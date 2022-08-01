/**
 * https://codeforces.com/contest/1352/problem/B
 * Time: O(K)
 * Space: O(K)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve() {

    int n, k;
    cin >> n >> k;

    if (k > n || ((n & 1) && !(k & 1)) || ((k & 1) && !(n & 1) && 2 * k > n)) {
        cout << "NO \n";
        return;
    }

    vector<int> res;
    if (!(n & 1) && (k & 1)) {
        while (k > 1) {
            res.push_back(2);
            n -= 2, k--;
        }
        res.push_back(n);
    } else {
        while (k > 1) {
            res.push_back(1);
            n--, k--;
        }
        res.push_back(n);
    }

    cout << "YES \n";
    for (int x : res)
        cout << x << ' ';
    cout << '\n';
}

int main() {

    int t;
    cin >> t;

    while (t--)
        solve();
}