/**
 * https://codeforces.com/contest/433/problem/B
 * Time: O(NlogN + M)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int v[n];
    for (int i = 0; i < n; ++i)
        cin >> v[i];

    ll ps_one[n + 1], ps_two[n + 1];
    ps_one[0] = 0, ps_two[0] = 0;

    for (int i = 0; i < n; ++i)
        ps_one[i + 1] = ps_one[i] + v[i];

    sort(v, v + n);

    for (int i = 0; i < n; ++i)
        ps_two[i + 1] = ps_two[i] + v[i];

    int m;
    cin >> m;

    while (m--) {

        int l, r, type;
        cin >> type >> l >> r;

        if (type == 1)
            cout << ps_one[r] - ps_one[l - 1];
        else
            cout << ps_two[r] - ps_two[l - 1];

        cout << '\n';
    }
}