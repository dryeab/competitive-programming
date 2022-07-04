/**
 * https://codeforces.com/problemset/problem/441/A
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, v;
    cin >> n >> v;

    int count = 0;
    vector<int> q;

    for (int i = 1; i <= n; ++i) {
        int k, can = 0, x;
        cin >> k;

        for (int j = 0; j < k; ++j) {
            cin >> x;
            if (x < v)
                can = 1;
        }

        if (can) {
            count++;
            q.push_back(i);
        }
    }

    cout << count << endl;
    for (auto x : q)
        cout << x << " ";
}