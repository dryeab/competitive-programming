/**
 * https://codeforces.com/problemset/problem/1511/C
 * Time: O(n + q)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, q, x, t;
    cin >> n >> q;

    vector<int> idx(51);
    for (int i = 1; i <= n; ++i) {
        cin >> x;
        if (idx[x] == 0)
            idx[x] = i;
    }

    for (int i = 0; i < q; ++i) {

        cin >> t;
        cout << idx[t] << ' ';

        for (int j = 1; j < 51; ++j) {
            if (idx[j] < idx[t])
                idx[j]++;
        }

        idx[t] = 1;
    }
}