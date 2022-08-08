/**
 * https://codeforces.com/problemset/problem/580/A
 * Time: O(N)
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

    vector<int> a(n);
    for (int &i : a)
        cin >> i;

    int res = 1, cur = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] >= a[i - 1])
            cur++;
        else
            cur = 1;
        res = max(res, cur);
    }

    cout << res;
}