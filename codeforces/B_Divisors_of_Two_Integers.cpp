/**
 * https://codeforces.com/contest/1108/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int N = 1e4 + 5;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, y = 0, x;
    cin >> n;

    vector<int> d(N);
    for (int i = 0; i < n; ++i) {
        cin >> x;
        d[x]++;
        y = max(y, x);
    }

    for (int i = 1; i <= y; ++i) {
        if (y % i == 0) {
            d[i] -= 1;
        }
    }

    for (int i = 1; i <= y; ++i) {
        if (d[i])
            x = i;
    }

    cout << x << ' ' << y;
}