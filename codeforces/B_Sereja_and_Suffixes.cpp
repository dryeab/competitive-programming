/**
 * https://codeforces.com/problemset/problem/368/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 1;
int visited[N] = {};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), ps(n, 1);
    for (int &i : a)
        cin >> i;

    visited[a[n - 1]] = 1;
    for (int i = n - 2; i >= 0; --i) {
        ps[i] = ps[i + 1] + (visited[a[i]] == 0);
        visited[a[i]] = 1;
    }

    int l;
    for (int i = 0; i < m; ++i) {
        cin >> l;
        cout << ps[l - 1] << endl;
    }
}