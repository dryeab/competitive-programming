/**
 * https://codeforces.com/problemset/problem/25/A
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    int cnt[] = {0, 0}, even, odd;
    for (int i = 1; i <= n; ++i) {
        cin >> x;
        cnt[x & 1]++;
        if (x & 1)
            odd = i;
        else
            even = i;
    }

    cout << (cnt[0] == 1 ? even : odd);
}