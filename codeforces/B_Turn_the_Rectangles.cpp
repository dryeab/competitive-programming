/**
 * https://codeforces.com/problemset/problem/1008/B
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, w, h, last = 1e9 + 5;
    cin >> n;

    bool isPos = true;
    for (int i = 0; i < n; ++i) {
        cin >> w >> h;
        if (min(w, h) > last)
            isPos = false;
        else if (max(w, h) <= last)
            last = max(w, h);
        else
            last = min(w, h);
    }

    cout << (isPos ? "YES" : "NO") << endl;
}