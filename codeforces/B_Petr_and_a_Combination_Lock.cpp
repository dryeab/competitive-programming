/**
 * https://codeforces.com/contest/1097/problem/B
 * Time: O(2^n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    for (int i = 0; i < (1 << n); ++i) {
        int res = 0;
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j))
                res += a[j];
            else
                res -= a[j];
        }
        if (res % 360 == 0) {
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";
}