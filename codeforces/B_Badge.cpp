/**
 * https://codeforces.com/problemset/problem/1020/B
 * Time: O(n^2)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> p(n + 1);

    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    for (int i = 1; i <= n; ++i) {

        int j = i;
        vector<int> visited(n + 1);

        while (visited[j] == 0) {
            visited[j] = 1;
            j = p[j];
        }

        cout << j << " ";
    }
}