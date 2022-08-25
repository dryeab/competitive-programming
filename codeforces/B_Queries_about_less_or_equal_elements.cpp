/**
 * https://codeforces.com/problemset/problem/600/B
 * Time: O(NlogN + MlogN)
 * Space: O(N + M)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m);

    for (int &i : a)
        cin >> i;

    for (int &i : b)
        cin >> i;

    sort(a.begin(), a.end());

    for (int i = 0; i < m; ++i)
        cout << upper_bound(a.begin(), a.end(), b[i]) - a.begin() << ' ';
}