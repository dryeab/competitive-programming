/**
 * https://codeforces.com/problemset/problem/327/A
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int x, cnt = 0, cur = 0, res = -1;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (cur < 0)
            cur = 0;
        cur += (x == 1 ? -1 : 1);
        res = max(res, cur);
        cnt += x;
    }

    cout << cnt + res;
}