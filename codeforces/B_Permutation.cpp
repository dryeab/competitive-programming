/**
 * https://codeforces.com/problemset/problem/137/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x, res = 0;
    cin >> n;

    vector<int> store(n + 1);
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x > n || store[x])
            res++;
        else
            store[x] = 1;
    }

    cout << res << endl;
}