/**
 * https://codeforces.com/problemset/problem/1365/A
 * Time: O(nm)
 * Space: O(max(n, m))
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n, m, x;
        cin >> n >> m;

        vector<int> row(n), col(m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> x;
                if (x) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        int left = min(count(row.begin(), row.end(), 0), count(col.begin(), col.end(), 0));

        if (left & 1)
            cout << "Ashish";
        else
            cout << "Vivek";
        cout << '\n';
    }
}