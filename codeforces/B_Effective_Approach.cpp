/**
 * https://codeforces.com/problemset/problem/227/B
 * Time: O(n + m)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x, m;
    cin >> n;

    vector<int> idx(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> x;
        idx[x] = i;
    }

    cin >> m;
    ll vas = 0, pet = 0;
    for (int i = 0; i < m; ++i) {
        cin >> x;
        vas += idx[x];
        pet += n - idx[x] + 1;
    }

    cout << vas << ' ' << pet;
}