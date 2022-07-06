/**
 * https://codeforces.com/problemset/problem/158/B
 * Time: O(n)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    int count[5] = {};
    while (n--) {
        cin >> x;
        count[x]++;
    }

    int res = 0;

    res += count[4] + count[3] + count[2] / 2;
    count[1] -= min(count[1], count[3]);

    if (count[2] & 1) {
        res++;
        count[1] -= min(2, count[1]);
    }

    res += (count[1] + 3) / 4;

    cout << res << endl;
}