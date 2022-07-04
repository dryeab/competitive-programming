/**
 * https://codeforces.com/contest/1225/problem/B2
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 5;

int a[N];

void solve() {

    int n, k, d;
    cin >> n >> k >> d;

    map<int, int> shows;
    int count = 0, res = n;

    for (int i = 0; i < n; ++i) {

        cin >> a[i];
        shows[a[i]]++;

        if (shows[a[i]] == 1)
            count++;

        if (i >= d) {
            shows[a[i - d]]--;
            if (shows[a[i - d]] == 0)
                count--;
        }

        if (i >= d - 1)
            res = min(res, count);
    }

    cout << res << endl;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--)
        solve();
}